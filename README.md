# Jaime Yan public content

Public articles and article assets for https://jaimeyan.com, plus the automation that reviews and publishes them.

The Astro application, UI source, private drafts, and unrelated internal tools remain in the private `yanmingyu92/portfolio` repository. This repository has an independent, fresh history; no private repository history or credential files belong here.

## Source layout

- `content/posts/`: published articles only. Do not commit `draft: true` files.
- `public/audio/`, `public/figures/`, `public/images/posts/`: public article assets.
- `tools/pharma-daily/`: daily evidence collection and draft generation.
- `tools/video/`: article companion rendering and YouTube publishing.
- `scripts/`: content QC, scheduled release, and syndication helpers.

## Local verification

```bash
npm ci
npm run qc:blog
npm run qc:assets
cd tools/video && npm ci && uv sync
```

The website build itself stays in the private site repository. A successful content merge triggers a production redeploy; the site build clones this repository and synchronizes the published content.

## Automation and secrets

Publishing workflows use the trusted Windows `pharma` self-hosted runner because the GitHub account currently cannot allocate hosted runners. Only `main`, schedules, manual dispatches, and merged-PR events execute on it. Fork pull requests never execute on the self-hosted runner; `content-qc` is manual-only, and daily content is checked before its review PR is created. The machine must remain online for scheduled jobs.

The runner reuses local resources instead of duplicating credentials into GitHub:

- `PRIVATE_SITE_ROOT` points to the private checkout for due drafts.
- `VIDEO_TOOL_ROOT` points to the private `tools/video/` OAuth directory.
- `deploy-site` uses `VERCEL_DEPLOY_HOOK_URL` when configured, otherwise the existing local Vercel CLI session to redeploy private `main`.
- `DEV_TO_API_KEY` is still required for actual dev.to publication; without it the workflow performs a safe dry run.
- Optional `KIMI_API` and `DEEPSEEK_KEY` enable the LLM editorial pass. Set `PHARMA_AGENT=1` only when these are configured.

Never commit OAuth JSON, `.env` files, access tokens, private drafts, or local rendering caches. Existing secrets cannot be read back through GitHub; rotate them through the UI when needed.

## Video operations

```bash
npm run video:build -- <slug> --script-only
npm run video:release -- <slug> --public
npm run video:publish-existing            # read-only visibility audit
npm run video:publish-existing -- --confirm  # make published posts' private videos public
```

The visibility utility never re-uploads a video and does not change unlisted videos.

## Rights

Public visibility is not a blanket open-source license. Copyright and any content-specific license notices remain with their respective owners.
