import re
import sys
from collections import Counter, defaultdict

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

shablon = re.compile(
    r"^(?P<ip>\d+\.\d+\.\d+\.\d+)"      # IP на початку рядка
    r".*?"                               # « - - » між полями
    r"\[(?P<chas>[^\]]+)\]"              # час у квадратних дужках
    r'\s+"(?P<metod>[A-Z]+)'             # метод — перше слово в лапках
    r"\s+(?P<shlyah>\S+)"                # шлях — друге слово
    r'[^"]*"'                            # протокол: пропустити до закривальної лапки
    r"\s+(?P<kod>\d{3})\b"               # код — рівно три цифри
)

rozibrano = 0
propusheno = 0
ip = Counter()
kody = Counter()
pomylky_5xx = []                         # (час, шлях)
shlyahy_5xx = Counter()
shlyahy_404 = Counter()
ip_404 = defaultdict(Counter)            # шлях -> Counter(ip)

with open("data/access.log", encoding="utf-8") as f:
    for ryadok in f:
        m = shablon.search(ryadok)
        if not m:
            propusheno += 1
            continue
        rozibrano += 1
        ip[m["ip"]] += 1
        kody[m["kod"]] += 1
        if m["kod"].startswith("5"):
            pomylky_5xx.append((m["chas"], m["shlyah"]))
            shlyahy_5xx[m["shlyah"]] += 1
        if m["kod"] == "404":
            shlyahy_404[m["shlyah"]] += 1
            ip_404[m["shlyah"]][m["ip"]] += 1

print("1. Розібрано / пропущено")
print(f"   розібрано {rozibrano}, пропущено {propusheno}")

print("\n2. Топ-5 IP за кількістю запитів")
for adresa, kilkist in ip.most_common(5):
    print(f"   {kilkist:>3}  {adresa}")

print("\n3. Запити за кодами відповіді")
for kod, kilkist in sorted(kody.items()):
    print(f"   {kod}: {kilkist}")
print(f"   (різних кодів: {len(kody)})")

print(f"\n4. Запити з помилкою 5xx: {len(pomylky_5xx)}")
for chas, shlyah in pomylky_5xx:
    print(f"   {chas}  {shlyah}")

print("\n   5xx за шляхами:")
for shlyah, kilkist in shlyahy_5xx.most_common():
    print(f"   {kilkist:>3}  {shlyah}")

print("\n   404: шлях → скільки разів (хто ходить)")
for shlyah, kilkist in shlyahy_404.most_common():
    hto = ", ".join(f"{a}×{n}" for a, n in ip_404[shlyah].most_common())
    print(f"   {kilkist:>3}  {shlyah}   [{hto}]")
