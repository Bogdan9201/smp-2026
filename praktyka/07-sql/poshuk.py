"""⭐3: пошук клієнтів за країною. Значення передається параметром (?), а не вклеюється в рядок.

    python praktyka/07-sql/poshuk.py
"""
import sqlite3
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

BAZA = Path(__file__).resolve().parents[2] / "data" / "chinook.db"
con = sqlite3.connect(f"file:{BAZA}?mode=ro", uri=True)

krayina = input("Країна: ").strip()
ryadky = con.execute(
    "SELECT FirstName, LastName FROM Customer WHERE Country = ?", (krayina,)
).fetchall()

if not ryadky:
    print(f"Клієнтів із країни «{krayina}» немає.")
else:
    print(f"Клієнтів: {len(ryadky)}")
    for imia, prizvyshche in ryadky:
        print(imia, prizvyshche)
