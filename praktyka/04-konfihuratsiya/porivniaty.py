import json
import sys
import tomllib
from pathlib import Path

import yaml

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

TEKA = Path(__file__).parent


def chytaty():
    with open(TEKA / "config.json", encoding="utf-8") as f:
        j = json.load(f)
    with open(TEKA / "config.yaml", encoding="utf-8") as f:
        y = yaml.safe_load(f)
    with open(TEKA / "config.toml", "rb") as f:
        t = tomllib.load(f)
    return {"JSON": j, "YAML": y, "TOML": t}


def splostyty(dani, prefiks=""):
    """Перетворює вкладені словники й списки на плоский словник шлях -> значення."""
    rezultat = {}
    if isinstance(dani, dict):
        for k, v in dani.items():
            rezultat.update(splostyty(v, f"{prefiks}.{k}" if prefiks else k))
    elif isinstance(dani, list):
        for i, v in enumerate(dani):
            rezultat.update(splostyty(v, f"{prefiks}[{i}]"))
    else:
        rezultat[prefiks] = dani
    return rezultat


def main():
    dzherela = chytaty()
    if dzherela["JSON"] == dzherela["YAML"] == dzherela["TOML"]:
        print("✅ однакові")
        return 0
    ploski = {nazva: splostyty(d) for nazva, d in dzherela.items()}
    vsi_kliuchi = sorted(set().union(*ploski.values()))
    for kliuch in vsi_kliuchi:
        znachennia = [ploski[n].get(kliuch, "— немає —") for n in ploski]
        # порівнюємо разом із типом, щоб 1 і "1" не вважались однаковими
        oznaky = {(type(z).__name__, repr(z)) for z in znachennia}
        if len(oznaky) > 1:
            print(f"❌ {kliuch}")
            for nazva, z in zip(ploski, znachennia):
                print(f"     {nazva:5} {z!r}")
    return 1


if __name__ == "__main__":
    sys.exit(main())