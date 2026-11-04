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

The website build itself stays in the private site repository. A successful content merge triggers its Vercel deploy hook; the site build clones this repository and synchronizes the published content.

## Automation and secrets

Workflows use GitHub-hosted Ubuntu runners. They never use a self-hosted runner on this public repository.

Required secrets are configured in repository Settings > Secrets and variables > Actions:

- `VERCEL_DEPLOY_HOOK_URL`: production deploy hook for the private site.
- `PORTFOLIO_READ_TOKEN`: fine-grained token with read-only Contents access to `yanmingyu92/portfolio`, used only to import due private drafts.
- `YOUTUBE_CLIENT_SECRET_JSON`, `YOUTUBE_TOKEN_JSON`: YouTube upload and visibility management.
- `DEV_TO_API_KEY`: dev.to weekly publishing.
- Optional `KIMI_API` and `DEEPSEEK_KEY`: LLM editorial passes. Set variable `PHARMA_AGENT=1` only when these are configured.

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
