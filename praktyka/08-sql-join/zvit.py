"""⭐3. Звіт: виторг за країнами -> zvit.md (таблиця Markdown).
Запуск з кореня репозиторію:  python praktyka/08-sql-join/zvit.py
"""
import sqlite3
from pathlib import Path

TUT = Path(__file__).resolve().parent
BAZA = TUT.parents[1] / "data" / "chinook.db"

ZAPYT = """
SELECT BillingCountry, ROUND(SUM(Total), 2) AS suma
FROM Invoice
GROUP BY BillingCountry
ORDER BY suma DESC
"""

con = sqlite3.connect(f"file:{BAZA}?mode=ro", uri=True)
ryadky = con.execute(ZAPYT).fetchall()

riadky_md = ["# Виторг за країнами", "", "| Країна | Виторг |", "|---|---:|"]
for krayina, suma in ryadky:
    riadky_md.append(f"| {krayina} | {suma:.2f} |")

(TUT / "zvit.md").write_text("\n".join(riadky_md) + "\n", encoding="utf-8")
print(f"Записано zvit.md: {len(ryadky)} країн")
