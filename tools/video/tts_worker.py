"""edge-tts worker: synthesizes a job file of segments to mp3 + word-timing json.

Job schema: {"segments": [{"id", "text", "voice", "rate", "mp3", "words"}]}
Word timings use edge-tts 100-ns offset/duration units.
"""
import asyncio
import json
import os
import sys

import edge_tts

MAX_ATTEMPTS = 3
BACKOFF_SEC = 5


async def synth(seg: dict) -> None:
    com = edge_tts.Communicate(text=seg["text"], voice=seg["voice"], rate=seg.get("rate", ""))
    words = []
    with open(seg["mp3"], "wb") as f:
        async for chunk in com.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                words.append({"t": chunk["text"], "o": chunk["offset"], "d": chunk["duration"]})
    with open(seg["words"], "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=True)


async def synth_with_retry(seg: dict) -> None:
    """Retry transient edge-tts failures (e.g. NoAudioReceived) per segment,
    and never leave a partial mp3/words file that the cache would mistake
    for a completed segment."""
    last = None
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            await synth(seg)
            return
        except Exception as e:  # noqa: BLE001 - report and retry any TTS failure
            last = e
            for p in (seg["mp3"], seg["words"]):
                if os.path.exists(p):
                    os.remove(p)
            if attempt < MAX_ATTEMPTS:
                await asyncio.sleep(BACKOFF_SEC * attempt)
    raise last


async def main() -> None:
    job_path = sys.argv[1]
    with open(job_path, encoding="utf-8") as f:
        job = json.load(f)
    failures = []
    for seg in job["segments"]:
        try:
            await synth_with_retry(seg)
        except Exception as e:  # noqa: BLE001 - keep synthesizing the rest
            failures.append((seg["id"], str(e)))
    if failures:
        for seg_id, err in failures:
            print(f"FAILED {seg_id}: {err}", file=sys.stderr)
        sys.exit(1)
    print(f"OK {len(job['segments'])}")


if __name__ == "__main__":
    asyncio.run(main())
