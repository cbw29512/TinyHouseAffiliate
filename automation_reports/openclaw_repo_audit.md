# OpenClaw Local Repo Audit

**Generated at:** 2026-04-20 15:40:59
**Repository:** `C:\Users\divcl\OneDrive\Desktop\TinyHouseAffiliate`
**Branch:** `main`

## Git Status

```text
?? automation_reports/
```

## Repository File Inventory

- `README.md`
- `core/schema.py`

## Top-Level Directory Listing

- **dir:** `automation_reports`
- **dir:** `core`
- **file:** `README.md`

## What This Project Appears To Be

Based only on files currently present, this appears to be an early-stage TinyHouseAffiliate automation repo. This report avoids inventing architecture that is not visible in the repository.

## Top-Level File Previews

### `README.md`

```text
# TinyHouseAffiliate

A GitHub-native high-ticket affiliate automation machine for tiny-home content.

## Current MVP

Provider:
- Craftsman Tiny Homes

First model:
- The Summit - Modular ADU

## Pipeline

1. Data schema
2. Provider config
3. Scraper
4. Asset downloader
5. FFmpeg video engine
6. YouTube metadata generator
7. CTA and affiliate disclosure
8. Future Shorts/Reels/TikTok verticalizer

## Architecture Rule

State and schema first. Functions second.

## Local Validation

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python tests/test_schema_validation.py
```

## Compliance Reminder

Only publish provider images and affiliate links after approval and according to the affiliate agreement.
```

## Missing Production Essentials

- Definition of Done for the first production milestone.
- Data schema for providers, tiny-home models, images, affiliate links, videos, and publishing state.
- Read-only provider inventory workflow.
- Validation scripts.
- GitHub Actions workflow.
- Secrets policy.

## Smallest Next 3 Safe Improvements

1. Create `docs/DEFINITION_OF_DONE.md`.
2. Create `docs/DATA_SCHEMA.md`.
3. Create `data/providers.example.json` and a validator.

## Exact Files To Create Or Edit Next

- `README.md`
- `docs/DEFINITION_OF_DONE.md`
- `docs/DATA_SCHEMA.md`
- `data/providers.example.json`
- `scripts/validate_state.ps1`

## Risks / Unknowns

- Affiliate terms and scraping permissions must be verified.
- Provider image usage rights must be clear.
- Publishing workflows should remain human-approved until the pipeline is proven.
- The repo is too early for unsupervised public posting.
