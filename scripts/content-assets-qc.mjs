#!/usr/bin/env node
// Validate public-content boundaries and article-owned local assets.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const postsDir = path.join(root, 'content', 'posts');
const ownedPrefixes = ['/audio/', '/figures/', '/images/posts/'];
let errors = 0;
let count = 0;

function fail(file, message) {
  errors += 1;
  console.error(`ERROR ${file}: ${message}`);
}

for (const name of fs.readdirSync(postsDir).filter((file) => file.endsWith('.md')).sort()) {
  const file = path.join(postsDir, name);
  const raw = fs.readFileSync(file, 'utf8');
  count += 1;
  if (/^draft:\s*true\s*$/m.test(raw)) fail(name, 'draft content must remain in the private repository');
  const video = raw.match(/^videoId:\s*(\S+)\s*$/m);
  if (video && !/^[A-Za-z0-9_-]{11}$/.test(video[1])) fail(name, `invalid YouTube videoId: ${video[1]}`);

  const refs = new Set();
  for (const match of raw.matchAll(/(?:\]\(|src=["']|href=["'])(\/(?:audio|figures|images\/posts)\/[^)\s"']+)/g)) refs.add(match[1]);
  const audio = raw.match(/^audioPath:\s*(\/audio\/\S+)\s*$/m);
  if (audio) refs.add(audio[1]);
  for (const ref of refs) {
    if (!ownedPrefixes.some((prefix) => ref.startsWith(prefix))) continue;
    const relative = ref.slice(1).split('/').join(path.sep);
    const target = path.resolve(root, 'public', relative);
    if (!target.startsWith(path.resolve(root, 'public') + path.sep)) fail(name, `unsafe asset path: ${ref}`);
    else if (!fs.existsSync(target) || !fs.statSync(target).isFile()) fail(name, `missing asset: ${ref}`);
  }
}

console.log(`${count} published post(s), ${errors} error(s)`);
process.exitCode = errors ? 1 : 0;
