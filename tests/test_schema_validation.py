"""
Unit tests for TinyHouseAffiliate schema contracts.

These tests protect the state-first architecture:
- JSON examples must validate.
- Hero asset lookup must work.
- Gallery assets must return in display order.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Type

from pydantic import BaseModel

from core.schema import AssetRole, ContentPackage, ProviderConfig


def load_json(path: str) -> Any:
    """Load a repository-local JSON fixture."""

    with Path(path).open("r", encoding="utf-8-sig") as file:
        return json.load(file)


def validate_model(model_cls: Type[BaseModel], data: Any) -> BaseModel:
    """Support both Pydantic v1 and v2 validation APIs."""

    if hasattr(model_cls, "model_validate"):
        return model_cls.model_validate(data)

    return model_cls.parse_obj(data)


def test_content_package_sample_validates() -> None:
    """The sample content package should match core/schema.py."""

    data = load_json("data/sample_content_package.json")
    package = validate_model(ContentPackage, data)

    assert package.home.slug == "the-summit-modular-adu"
    assert package.accessory_kit.home_slug == package.home.slug
    assert len(package.accessory_kit.products) == 1


def test_hero_asset_lookup_returns_first_hero() -> None:
    """TinyHomeModel.hero_asset should return the hero asset."""

    data = load_json("data/sample_content_package.json")
    package = validate_model(ContentPackage, data)

    hero = package.home.hero_asset()

    assert hero is not None
    assert hero.role == AssetRole.HERO
    assert hero.order == 0


def test_gallery_assets_return_gallery_only() -> None:
    """TinyHomeModel.gallery_assets should exclude hero assets."""

    data = load_json("data/sample_content_package.json")
    package = validate_model(ContentPackage, data)

    gallery = package.home.gallery_assets()

    assert len(gallery) == 1
    assert gallery[0].role == AssetRole.GALLERY


def test_provider_config_sample_validates() -> None:
    """Provider config sample should match ProviderConfig."""

    data = load_json("data/sample_provider_config.json")
    provider = validate_model(ProviderConfig, data)

    assert provider.provider_key == "craftsman_tiny_homes"
    assert provider.provider_name == "Craftsman Tiny Homes"


if __name__ == "__main__":
    test_content_package_sample_validates()
    test_hero_asset_lookup_returns_first_hero()
    test_gallery_assets_return_gallery_only()
    test_provider_config_sample_validates()
    print("All schema validation tests passed.")
