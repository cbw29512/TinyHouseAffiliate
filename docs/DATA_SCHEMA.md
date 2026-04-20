# Data Schema

## Purpose

This document defines the state model for the TinyHouseAffiliate automation pipeline before expanding functions.

The system should treat JSON state as the source of truth.

## Provider Schema

```json
{
  "provider_id": "craftsman_tiny_homes",
  "provider_name": "Craftsman Tiny Homes",
  "website_url": "https://example.com",
  "affiliate_status": "unknown",
  "scraping_permission": "unknown",
  "image_usage_permission": "unknown",
  "notes": "Do not publish provider images or affiliate links until terms are verified."
}
```

## Tiny Home Model Schema

```json
{
  "model_id": "summit_modular_adu",
  "provider_id": "craftsman_tiny_homes",
  "model_name": "The Summit - Modular ADU",
  "source_url": "",
  "hero_image_url": "",
  "gallery_image_urls": [],
  "price_text": "",
  "square_feet": null,
  "bedrooms": null,
  "bathrooms": null,
  "features": [],
  "status": "draft",
  "last_checked_at": null
}
```

## Content Asset Schema

```json
{
  "asset_id": "summit_modular_adu_youtube_long_001",
  "model_id": "summit_modular_adu",
  "content_type": "youtube_long",
  "title": "",
  "description": "",
  "disclosure": "This content may contain affiliate links. Publishing requires human approval.",
  "video_path": "",
  "thumbnail_path": "",
  "status": "draft",
  "created_at": null,
  "approved_at": null,
  "published_at": null
}
```

## Status Values

Use these values consistently:

```text
draft
needs_review
approved
rejected
published
archived
```

## Safety Rules

- Never store API keys or affiliate secrets in JSON.
- Never mark content as published unless it was actually published.
- Never use provider images unless permission is verified.
- Never auto-publish without human approval.
- Keep scraped or provider data separate from generated content.
