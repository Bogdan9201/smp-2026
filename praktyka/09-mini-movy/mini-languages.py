"""Робота 9: звіт про файли в теці — пʼять міні-мов усередині Python.

Запуск (з кореня репозиторію):
    python praktyka/09-mini-movy/mini-languages.py
    python praktyka/09-mini-movy/mini-languages.py data

Перевірка:
    python praktyka/09-mini-movy/perevir.py
"""

import glob
import os
import re
import sys
from datetime import datetime

PAPKA = sys.argv[1] if len(sys.argv) > 1 else "."

# ── Мова 1: glob — шаблон імені файлу ────────────────────────────────
elementy = glob.glob(os.path.join(PAPKA, "*"))
fayly = [f for f in elementy if os.path.isfile(f)]

# ── Мова 2: зріз — лише 10 найбільших ────────────────────────────────
fayly.sort(key=os.path.getsize, reverse=True)
top = fayly[:10]

# ── Мова 3: формат рядків ────────────────────────────────────────────
print(f"{'Файл':<30}{'КБ':>8}  Змінено")
print("-" * 50)

for shliakh in top:
    imia = os.path.basename(shliakh)
    kb = os.path.getsize(shliakh) / 1024
    zmineno = datetime.fromtimestamp(os.path.getmtime(shliakh))

    # ── Мова 4: формат дати ──────────────────────────────────────────
    data = zmineno.strftime("%d.%m.%Y")

    print(f"{imia:<30}{kb:>8.1f}  {data}")

# ── Мова 5: регулярний вираз ─────────────────────────────────────────
# Рівно 4 цифри - 2 цифри - 2 цифри.
DATA_V_NAZVI = re.compile(r"\d{4}-\d{2}-\d{2}")

z_datoyu = [
    f
    for f in fayly
    if DATA_V_NAZVI.search(os.path.basename(f))
]

print("-" * 50)
print(f"Файлів у теці: {len(fayly)}")
print(f"З датою в назві: {len(z_datoyu)}")
