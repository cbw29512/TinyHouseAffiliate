"""
Core schema for TinyHouseAffiliate.

State comes first:
- TinyHomeModel describes the house we are promoting.
- AmazonProduct describes an item that can outfit that house.
- ContentPackage joins house + accessories into one affiliate content unit.
"""

from __future__ import annotations

import logging
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field, HttpUrl


logger = logging.getLogger(__name__)


class AssetRole(str, Enum):
    """Purpose of an image/media asset in the video pipeline."""

    HERO = "hero"
    GALLERY = "gallery"
    CTA_BACKGROUND = "cta_background"


class HomeAsset(BaseModel):
    """One media asset from a tiny-home model page."""

    source_url: HttpUrl
    role: AssetRole
    order: int = Field(default=0, ge=0)
    local_path: Optional[str] = None
    alt_text: Optional[str] = None


class TinyHomeModel(BaseModel):
    """Contract shared by scraper, page generator, and video engine."""

    provider_key: str
    model_name: str
    slug: str
    source_url: HttpUrl
    price_text: Optional[str] = None
    square_feet_text: Optional[str] = None
    dimensions_text: Optional[str] = None
    short_description: Optional[str] = None
    features: List[str] = Field(default_factory=list)
    assets: List[HomeAsset] = Field(default_factory=list)
    affiliate_url: Optional[HttpUrl] = None
    cta_text: str = "Check the description to learn more or request information."

    def hero_asset(self) -> Optional[HomeAsset]:
        """Return the first front-of-house hero asset."""

        try:
            heroes = [asset for asset in self.assets if asset.role == AssetRole.HERO]
            heroes.sort(key=lambda asset: asset.order)
            return heroes[0] if heroes else None
        except Exception as exc:
            logger.exception("Hero asset lookup failed for %s", self.slug)
            raise RuntimeError(f"Hero asset lookup failed for {self.slug}") from exc

    def gallery_assets(self) -> List[HomeAsset]:
        """Return slideshow assets in display order."""

        try:
            gallery = [asset for asset in self.assets if asset.role == AssetRole.GALLERY]
            gallery.sort(key=lambda asset: asset.order)
            return gallery
        except Exception as exc:
            logger.exception("Gallery asset lookup failed for %s", self.slug)
            raise RuntimeError(f"Gallery asset lookup failed for {self.slug}") from exc


class AmazonProduct(BaseModel):
    """Curated or PA-API-sourced Amazon item for a tiny-home kit."""

    category: str
    title: str
    search_phrase: str
    asin: Optional[str] = None
    why_it_fits: str
    priority: int = Field(default=50, ge=1, le=100)
    affiliate_url: Optional[HttpUrl] = None


class AccessoryKit(BaseModel):
    """A themed shopping kit that outfits a tiny home."""

    kit_name: str
    home_slug: str
    products: List[AmazonProduct] = Field(default_factory=list)


class ContentPackage(BaseModel):
    """One generated marketing package for a home + Amazon gear."""

    home: TinyHomeModel
    accessory_kit: AccessoryKit
    youtube_title: str
    youtube_description: str
    landing_page_path: str


class ProviderConfig(BaseModel):
    """Provider-specific configuration for future scraper plugins."""

    provider_key: str
    provider_name: str
    base_url: HttpUrl
    allowed_model_urls: List[HttpUrl] = Field(default_factory=list)
    notes: Optional[str] = None
