import sys
import tkinter as tk
from pathlib import Path

import yaml

TUT = Path(__file__).resolve().parent
TYPY = {"tekst", "parol", "chyslo"}


def zavantazhyty(shliakh):
    with open(shliakh, encoding="utf-8") as f:
        opys = yaml.safe_load(f)
    if not isinstance(opys, dict):
        raise ValueError("опис має бути словником (zaholovok, polia, praporci, knopky)")
    opys.setdefault("zaholovok", "")
    opys.setdefault("polia", [])
    opys.setdefault("praporci", [])
    opys.setdefault("knopky", [])
    for pole in opys["polia"]:
        if "pidpys" not in pole:
            raise ValueError(f"у полі {pole} немає pidpys")
        if pole.get("typ", "tekst") not in TYPY:
            raise ValueError(f"невідомий typ «{pole.get('typ')}» у полі «{pole['pidpys']}»; "
                             f"дозволені: {', '.join(sorted(TYPY))}")
    return opys


def stvoryty_pole(batko, pole):
    typ = pole.get("typ", "tekst")
    if typ == "parol":
        return tk.Entry(batko, show="•")
    if typ == "chyslo":
        return tk.Spinbox(batko, from_=0, to=9999)
    return tk.Entry(batko)


def zibraty_formu(korin, opys):
    """Усе розкладається grid-ом: рядок за рядком, два стовпці."""
    rjad = 0
    if opys["zaholovok"]:
        tk.Label(korin, text=opys["zaholovok"], font=("TkDefaultFont", 14, "bold")).grid(
            row=rjad, column=0, columnspan=2, pady=8)
        rjad += 1
    for pole in opys["polia"]:
        tk.Label(korin, text=pole["pidpys"] + ":").grid(
            row=rjad, column=0, sticky="e", padx=6, pady=3)
        stvoryty_pole(korin, pole).grid(row=rjad, column=1, sticky="ew", padx=6)
        rjad += 1
    for tekst in opys["praporci"]:
        tk.Checkbutton(korin, text=tekst).grid(row=rjad, column=1, sticky="w", padx=6, pady=3)
        rjad += 1
    if opys["knopky"]:
        ramka = tk.Frame(korin)
        ramka.grid(row=rjad, column=0, columnspan=2, sticky="e", padx=6, pady=8)
        for tekst in reversed(opys["knopky"]):      # side="right" розставляє з кінця
            tk.Button(ramka, text=tekst).pack(side="right", padx=(6, 0))
    korin.columnconfigure(1, weight=1)


def main():
    shliakh = Path(sys.argv[1]) if len(sys.argv) > 1 else TUT / "forma.yaml"
    if not shliakh.is_absolute() and not shliakh.exists():
        shliakh = TUT / shliakh
    try:
        opys = zavantazhyty(shliakh)
    except (OSError, ValueError, yaml.YAMLError) as pomylka:
        sys.exit(f"Не вдалося прочитати опис форми {shliakh}: {pomylka}")
    vikno = tk.Tk()
    vikno.title(opys["zaholovok"] or "Форма")
    zibraty_formu(vikno, opys)
    vikno.mainloop()


if __name__ == "__main__":
    main()
