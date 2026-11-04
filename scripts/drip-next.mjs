#!/usr/bin/env node
// Weekly drip planner — prints the queue entries due for release as JSON.
// An entry is due when its date <= today, its private source is still a draft,
// and no already-live public copy exists. DRIP_PRIVATE_POSTS_DIR is required
// only in the public content repository's scheduled release workflow.
// Usage: node scripts/drip-next.mjs [--date YYYY-MM-DD]   (default: today UTC)
import { readFileSync, existsSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const args = process.argv.slice(2);
const i = args.indexOf('--date');
const today = (i !== -1 && args[i + 1]) || new Date().toISOString().slice(0, 10);

const queue = JSON.parse(readFileSync(join(root, 'docs', 'drip-queue.json'), 'utf8'));
const privatePostsDir = process.env.DRIP_PRIVATE_POSTS_DIR;
const due = queue.filter(e => {
	if (e.date > today) return false;
	const publicPost = join(root, 'content', 'posts', `${e.slug}.md`);
	if (existsSync(publicPost) && !/^draft:\s*true\s*$/m.test(readFileSync(publicPost, 'utf8'))) return false;
	const privatePost = privatePostsDir && join(privatePostsDir, `${e.slug}.md`);
	const source = privatePost && existsSync(privatePost) ? privatePost : publicPost;
	return existsSync(source) && /^draft:\s*true\s*$/m.test(readFileSync(source, 'utf8'));
});
console.log(JSON.stringify(due));
