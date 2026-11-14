import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

LOG = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/access.log")

# час у квадратних дужках: 17/Mar/2026:08:01:26 +0200
CHAS = re.compile(r"\[([^\]]+)\]")
# коди strptime: %d день, %b скорочена назва місяця, %Y рік,
# %H:%M:%S час, %z зсув відносно UTC
FORMAT = "%d/%b/%Y:%H:%M:%S %z"

po_hodynakh = Counter()
propusheno = 0
for riadok in LOG.read_text(encoding="utf-8", errors="replace").splitlines():
    m = CHAS.search(riadok)
    if m is None:
        propusheno += 1
        continue
    try:
        chas = datetime.strptime(m[1], FORMAT)
    except ValueError:
        propusheno += 1
        continue
    po_hodynakh[chas.hour] += 1

if not po_hodynakh:
    sys.exit("У логу не знайдено жодного запиту з розбірним часом.")

najbilshe = max(po_hodynakh.values())
SHYRYNA = 40  # довжина найдовшого стовпчика
for god in range(24):
    n = po_hodynakh[god]
    if n == 0:
        continue
    stovpchyk = "#" * round(n / najbilshe * SHYRYNA)
    print(f"{god:02}:00 {stovpchyk:<{SHYRYNA}} {n:>4}")

najzavantazhenisha = max(po_hodynakh, key=po_hodynakh.get)
print(f"\nНайнавантаженіша година: {najzavantazhenisha:02}:00 "
      f"({po_hodynakh[najzavantazhenisha]} запитів)")
if propusheno:
    print(f"Пропущено рядків без розбірного часу: {propusheno}")
