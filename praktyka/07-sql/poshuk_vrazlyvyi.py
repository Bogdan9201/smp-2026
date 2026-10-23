"""⭐4: ВРАЗЛИВА копія poshuk.py — запит зібраний f-рядком. Не робіть так у справжніх програмах!

    python praktyka/07-sql/poshuk_vrazlyvyi.py
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
zapyt = f"SELECT FirstName, LastName FROM Customer WHERE Country = '{krayina}'"
print("SQL:", zapyt)
try:
    ryadky = con.execute(zapyt).fetchall()
except sqlite3.Error as e:
    print("Помилка SQL:", e)
    sys.exit(1)

if not ryadky:
    print(f"Клієнтів із країни «{krayina}» немає.")
else:
    print(f"Клієнтів: {len(ryadky)}")
    for imia, prizvyshche in ryadky:
        print(imia, prizvyshche)
