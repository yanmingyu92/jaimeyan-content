#!/usr/bin/env node
/**
 * auth-youtube.mjs — one-time YouTube OAuth authorization.
 *
 * Reads  tools/video/.google-client-secret.json  (Desktop app client, from Google Cloud Console)
 * Writes tools/video/.google-token.json          (refresh token; reused by upload-video.mjs)
 *
 * Run: node tools/video/auth-youtube.mjs
 */
import fs from 'node:fs';
import path from 'node:path';
import http from 'node:http';
import { exec } from 'node:child_process';
import { google } from 'googleapis';
import { TOOL_ROOT } from './lib/util.mjs';

const SECRET_PATH = path.join(TOOL_ROOT, '.google-client-secret.json');
const TOKEN_PATH = path.join(TOOL_ROOT, '.google-token.json');
const PORT = 39217;
const SCOPES = [
  'https://www.googleapis.com/auth/youtube.upload',
  // Needed to delete replaced uploads (e.g. the black-intro batch of
  // 2026-10-05). Superset of upload-only, so uploads keep working.
  'https://www.googleapis.com/auth/youtube',
];

if (!fs.existsSync(SECRET_PATH)) {
  console.error(`Missing ${SECRET_PATH}`);
  console.error('Download the OAuth client JSON from Google Cloud Console (Desktop app type) and save it there.');
  process.exit(1);
}

const { installed } = JSON.parse(fs.readFileSync(SECRET_PATH, 'utf8'));
const client = new google.auth.OAuth2(installed.client_id, installed.client_secret, `http://localhost:${PORT}`);

const server = http.createServer(async (req, res) => {
  const url = new URL(req.url, `http://localhost:${PORT}`);
  const code = url.searchParams.get('code');
  const err = url.searchParams.get('error');
  if (!code) {
    res.writeHead(400).end('No authorization code received' + (err ? `: ${err}` : ''));
    server.close();
    process.exit(1);
  }
  try {
    const { tokens } = await client.getToken(code);
    client.setCredentials(tokens);
    fs.writeFileSync(TOKEN_PATH, JSON.stringify(tokens, null, 2), 'utf8');
    // Upload-only scope need not grant channels.list. Saving a valid token is success.
    res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' }).end('<h3>Authorized</h3><p>Token saved. You can close this tab and return to the task.</p>');
    console.log('YouTube upload authorization saved.');
    console.log(`Token saved to ${TOKEN_PATH}`);
    server.close();
    process.exit(0);
  } catch (e) {
    res.writeHead(500).end('Token exchange failed: ' + e.message);
    server.close();
    process.exit(1);
  }
});

server.listen(PORT, () => {
  const authUrl = client.generateAuthUrl({
    access_type: 'offline',
    prompt: 'consent',
    scope: SCOPES,
  });
  console.log('Opening browser for YouTube authorization...');
  console.log(`If it does not open, visit:\n\n${authUrl}\n`);
  exec(`start "" "${authUrl}"`);
});
