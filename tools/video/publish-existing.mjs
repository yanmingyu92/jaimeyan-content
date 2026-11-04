#!/usr/bin/env node
/**
 * Audit YouTube visibility for videoId values on published posts.
 * Default: read-only. With --confirm: change only private videos to public.
 * Never re-uploads and never changes unlisted videos.
 */
import fs from 'node:fs';
import path from 'node:path';
import { google } from 'googleapis';
import { SITE_ROOT, TOOL_ROOT } from './lib/util.mjs';

const confirm = process.argv.slice(2).includes('--confirm');
const ids = new Map();
for (const name of fs.readdirSync(path.join(SITE_ROOT, 'content', 'posts')).filter((file) => file.endsWith('.md'))) {
  const raw = fs.readFileSync(path.join(SITE_ROOT, 'content', 'posts', name), 'utf8');
  if (/^draft:\s*true\s*$/m.test(raw)) continue;
  const match = raw.match(/^videoId:\s*([A-Za-z0-9_-]{11})\s*$/m);
  if (match) ids.set(match[1], name.replace(/\.md$/, ''));
}
if (!ids.size) throw new Error('No videoId values found on published posts.');

const credentialRoot = process.env.VIDEO_TOOL_ROOT || TOOL_ROOT;
const secretPath = path.join(credentialRoot, '.google-client-secret.json');
const tokenPath = path.join(credentialRoot, '.google-token.json');
if (!fs.existsSync(secretPath) || !fs.existsSync(tokenPath)) {
  console.error('YouTube OAuth files are missing. Run npm run video:auth first; never commit these files.');
  process.exit(1);
}
const secret = JSON.parse(fs.readFileSync(secretPath, 'utf8'));
const tokens = JSON.parse(fs.readFileSync(tokenPath, 'utf8'));
const client = new google.auth.OAuth2(secret.installed.client_id, secret.installed.client_secret, 'http://localhost');
client.setCredentials(tokens);
const youtube = google.youtube({ version: 'v3', auth: client });

async function listVideos(videoIds) {
  const found = new Map();
  for (let i = 0; i < videoIds.length; i += 50) {
    const response = await youtube.videos.list({ id: videoIds.slice(i, i + 50).join(','), part: 'status,snippet', maxResults: 50 });
    for (const video of response.data.items || []) found.set(video.id, video);
  }
  return found;
}

const allIds = [...ids.keys()];
const videos = await listVideos(allIds);
const candidates = [];
let failures = 0;
for (const [id, slug] of ids) {
  const video = videos.get(id);
  if (!video) {
    failures += 1;
    console.error(`MISSING ${id} ${slug}`);
  } else if (video.status.privacyStatus === 'private') {
    candidates.push(id);
    console.log(`PRIVATE ${id} ${slug}`);
  } else {
    console.log(`${video.status.privacyStatus.toUpperCase()} ${id} ${slug}`);
  }
}

console.log(`\n${ids.size} referenced video(s); ${candidates.length} private; ${failures} missing.`);
if (!confirm) {
  console.log('Read-only audit complete. Re-run with --confirm to make only the private videos public.');
  process.exitCode = failures ? 1 : 0;
} else {
  for (const id of candidates) {
    try {
      await youtube.videos.update({ part: 'status', requestBody: { id, status: { privacyStatus: 'public' } } });
      console.log(`PUBLISHED ${id} ${ids.get(id)}`);
    } catch (error) {
      failures += 1;
      console.error(`FAILED ${id} ${ids.get(id)} (${error.response?.status || error.code || 'unknown'}): ${error.message}`);
    }
  }
  const verified = await listVideos(candidates);
  for (const id of candidates) {
    if (verified.get(id)?.status?.privacyStatus !== 'public') {
      failures += 1;
      console.error(`VERIFY FAILED ${id} ${ids.get(id)}`);
    }
  }
  console.log(`Visibility update complete with ${failures} failure(s).`);
  process.exitCode = failures ? 1 : 0;
}
