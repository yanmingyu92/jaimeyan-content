"""Regression tests for extract.py against real 2026-09-04/05 window items.

Two bugs prompted these tests (found in human review of the 2026-09-05 brief):
1. A Phase 3 *failure* story ("Ionis-partnered drug") was classified as a
   'collaboration' deal and landed in the deals table.
2. `companies` was empty for every RSS deal, which produced the bogus
   'undisclosed party' label downstream in the deal-size figure.
"""
import sqlite3
from pathlib import Path

import pytest

from pharma_daily import extract

DB = Path(__file__).resolve().parents[1] / "data" / "pharma.db"

NOVARTIS_URL_FRAG = "novartis-lpa"


def _window_items() -> list[dict]:
    if not DB.exists():
        pytest.skip("pharma.db not available")
    db = sqlite3.connect(DB)
    db.row_factory = sqlite3.Row
    rows = db.execute(
        "SELECT * FROM items WHERE date BETWEEN '2026-09-04' AND '2026-09-05'"
    ).fetchall()
    db.close()
    if not rows:
        pytest.skip("no window items in pharma.db")
    return [dict(r) for r in rows]


@pytest.fixture(scope="module")
def deals():
    return extract.extract_deals(_window_items())


def test_phase3_failure_is_not_a_deal(deals):
    assert not any(NOVARTIS_URL_FRAG in d["source_url"] for d in deals), (
        "Novartis Lp(a) Phase 3 miss must not appear in the deals table"
    )


def test_classify_readout_beats_partnered_origin():
    t = ("Novartis Lp(a) drug fails to lower cardiovascular risk in closely "
         "watched ph. 3 trial Novartis' Ionis-partnered drug failed to reduce "
         "risk in the first late-stage test.")
    assert extract.classify(t) == "clinical-readout"


def test_menarini_parties_extracted(deals):
    m = [d for d in deals if "menarini" in (d.get("headline") or "").lower()]
    assert m, "Menarini/Gan & Lee deal missing"
    assert any("Menarini" in d["companies"] and "Gan & Lee" in d["companies"] for d in m), (
        f"companies should name both parties, got: {[d['companies'] for d in m]}"
    )
    assert any(d["total_usd"] == pytest.approx(771e6, rel=0.01) for d in m)


def test_neushen_financing_party(deals):
    n = [d for d in deals if "neushen" in (d.get("headline") or "").lower()]
    assert n, "NeuShen financing missing"
    assert any("NeuShen" in d["companies"] for d in n)


def test_html_entities_unescaped_in_parties():
    lic, lee = extract.find_parties(
        "Menarini signs $771M deal to take Gan &amp; Lee GLP-1 to European market"
    )
    assert lee is not None and "&amp;" not in lee + (lic or "")


def test_approval_still_not_a_deal():
    items = [{
        "source": "fda-press", "title": "FDA approves X for Y", "summary": "",
        "url": "u", "date": "2026-09-05",
    }]
    assert extract.extract_deals(items) == []


def test_classify_word_stems():
    # Alternatives are stems; a trailing \b after the group silently broke
    # inflected forms ("acquires", "approval", "collaborate") until 2026-09-06.
    assert extract.classify("FDA approves Xtandi expansion") == "approval"
    assert extract.classify("Acme to acquire BioCo for $2B") == "acquisition"
    assert extract.classify("X and Y announce collaboration on ADC") == "collaboration"
    assert extract.classify("Z reports topline Phase 3 results") == "clinical-readout"
    assert extract.classify("BioCo licenses platform to BigPharma") == "license"
