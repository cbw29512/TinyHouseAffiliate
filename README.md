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
