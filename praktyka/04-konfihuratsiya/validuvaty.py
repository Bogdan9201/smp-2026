import json
import sys
import tomllib
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

TEKA = Path(__file__).parent


def chytaty(imia):
    shliakh = TEKA / imia
    if shliakh.suffix == ".json":
        with open(shliakh, encoding="utf-8") as f:
            return json.load(f)
    if shliakh.suffix == ".yaml":
        with open(shliakh, encoding="utf-8") as f:
            return yaml.safe_load(f)
    with open(shliakh, "rb") as f:
        return tomllib.load(f)


def main():
    with open(TEKA / "schema.json", encoding="utf-8") as f:
        validator = Draft202012Validator(json.load(f))
    kod = 0
    for imia in ("config.json", "config.yaml", "config.toml"):
        dani = chytaty(imia)
        pomylky = sorted(validator.iter_errors(dani), key=lambda e: list(e.path))
        if not pomylky:
            print(f"✅ {imia}")
            continue
        kod = 1
        print(f"❌ {imia}")
        for p in pomylky:
            shliakh = ".".join(str(x) for x in p.path) or "(корінь)"
            print(f"     {shliakh}: {p.message}")
    return kod


if __name__ == "__main__":
    sys.exit(main())