import assert from 'node:assert/strict';
import { extractScript } from './lib/extract-script.mjs';
for (const table of ['| Need | Use |\n|---|---|\n| Backup | JSON |', '| Need | Use | Note |\n|---|---|---|\n| Backup | JSON | Editable |']) {
 const script = extractScript('---\ntitle: "Fixture"\ndate: 2026-09-20\n---\nIntro.\n\n## Exports\n\n'+table, 'synthetic-fixture');
 const text = script.chapters.flatMap(c=>c.slides).map(s=>s.narration).join('\n');
 assert(text.includes('Backup: JSON'));
 assert(!text.includes('undefined'));
 if(table.includes('Editable')) assert(text.includes('Editable'));
}
console.log('PASS two-column and three-column table narration preserves content without undefined values');
