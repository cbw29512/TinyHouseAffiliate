"""
Validate TinyHouseAffiliate local JSON state against core/schema.py.

This script is deterministic:
- It reads local JSON files.
- It validates them with Pydantic models.
- It logs clear success/failure messages.
- It exits non-zero on invalid state.
"""

from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path
from typing import Any, Type

from pydantic import BaseModel, ValidationError

from core.schema import ContentPackage, ProviderConfig


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)

logger = logging.getLogger(__name__)


def load_json(path: Path) -> Any:
    """Read a JSON file and return parsed Python data."""

    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError as exc:
        logger.exception("JSON file not found: %s", path)
        raise RuntimeError(f"JSON file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        logger.exception("Invalid JSON in file: %s", path)
        raise RuntimeError(f"Invalid JSON in file: {path}: {exc}") from exc


def validate_model(model_cls: Type[BaseModel], data: Any) -> BaseModel:
    """
    Validate data against a Pydantic model.

    Why this helper exists:
    - Pydantic v2 uses model_validate.
    - Pydantic v1 used parse_obj.
    - This keeps the script easier to run across environments.
    """

    try:
        if hasattr(model_cls, "model_validate"):
            return model_cls.model_validate(data)

        return model_cls.parse_obj(data)
    except ValidationError:
        logger.exception("Validation failed for model: %s", model_cls.__name__)
        raise


def main() -> int:
    """CLI entrypoint for local state validation."""

    parser = argparse.ArgumentParser(
        description="Validate TinyHouseAffiliate JSON state files."
    )

    parser.add_argument(
        "--content-package",
        default="data/sample_content_package.json",
        help="Path to a ContentPackage JSON file.",
    )

    parser.add_argument(
        "--provider-config",
        default="data/sample_provider_config.json",
        help="Path to a ProviderConfig JSON file.",
    )

    args = parser.parse_args()

    try:
        content_path = Path(args.content_package)
        provider_path = Path(args.provider_config)

        content_data = load_json(content_path)
        provider_data = load_json(provider_path)

        content_package = validate_model(ContentPackage, content_data)
        provider_config = validate_model(ProviderConfig, provider_data)

        hero = content_package.home.hero_asset()
        gallery = content_package.home.gallery_assets()

        logger.info("Validated content package: %s", content_package.home.slug)
        logger.info("Validated provider config: %s", provider_config.provider_key)
        logger.info("Hero asset found: %s", bool(hero))
        logger.info("Gallery asset count: %s", len(gallery))

        return 0
    except Exception as exc:
        logger.exception("State validation failed.")
        print(f"ERROR: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
