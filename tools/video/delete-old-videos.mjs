#!/usr/bin/env node
/**
 * delete-old-videos.mjs — one-off cleanup: delete the 19 superseded uploads
 * from the 2026-10-05 batch (black-intro bug). These IDs were replaced by
 * fixed re-uploads; the new IDs live in the posts' frontmatter.
 *
 * Requires .google-token.json authorized with the youtube (manage) scope —
 * re-run auth-youtube.mjs once after SCOPES was extended.
 */
import fs from 'node:fs';
import path from 'node:path';
import { google } from 'googleapis';
import { TOOL_ROOT } from './lib/util.mjs';

const OLD_IDS = [
  ['clinical-r-in-practice-roadmap', 'PoTNl--5UOM'],
  ['targets-reproducible-pipelines', 'nmu0_aqiZV4'],
  ['sas-to-r-migration-ledger', 'WytO-SpWmq8'],
  ['r-validation-risk-based-framework', '4R_6ujw9oz8'],
  ['quarto-clinical-study-reports', 'v54_tY2xWb4'],
  ['pharmaverse-ecosystem-map', 'ZknC9lawKwI'],
  ['natural-language-to-cdisc', '9HTH2OwA84E'],
  ['metadata-driven-development-metacore', 'q2VIgNsHuzg'],
  ['llm-clinical-coding-cases', '0Fe1KYOcpIo'],
  ['gxp-shiny-validation', 'GwfX0d-6cbs'],
  ['clinical-tables-showdown', 'SkUtGooqehs'],
  ['clinical-data-science-next-five-years', 'jpzqOaLtWWc'],
  ['clinical-data-flow-sdtm-to-submission', 'rUmqjlWryKA'],
  ['ard-analysis-results-data', 'tPrOBr0aWHI'],
  ['ai-agents-mcp-clinical-stack', '0IDUSq0sur8'],
  ['admiral-adam-lego-method', 'p7NsTeltZSI'],
  ['pharma-daily-2026-09-17', 'lTwZ-yz1sOI'],
  ['cdisc-ai-challenge-2026-synthetic-adam', 'J4_CLrjpqvw'],
  ['clinvista-gxp-shiny-governance', 'Gj_Bm1aIyl0'],
];

const secret = JSON.parse(fs.readFileSync(path.join(TOOL_ROOT, '.google-client-secret.json'), 'utf8'));
const tokens = JSON.parse(fs.readFileSync(path.join(TOOL_ROOT, '.google-token.json'), 'utf8'));
const client = new google.auth.OAuth2(secret.installed.client_id, secret.installed.client_secret);
client.setCredentials(tokens);
const yt = google.youtube({ version: 'v3', auth: client });

for (const [slug, id] of OLD_IDS) {
  try {
    await yt.videos.delete({ id });
    console.log(`DELETED ${id}  (${slug})`);
  } catch (e) {
    console.log(`FAILED  ${id}  (${slug}): ${e.message}`);
  }
}
