import re
import sys
from collections import Counter, defaultdict

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

shablon = re.compile(
    r"^(?P<ip>\d+\.\d+\.\d+\.\d+)"
    r".*?"
    r"\[(?P<chas>[^\]]+)\]"
    r'\s+"(?P<metod>[A-Z]+)'
    r"\s+(?P<shlyah>\S+)"
    r'[^"]*"'
    r"\s+(?P<kod>\d{3})\b"
)

uspishni = Counter()                 # ⭐1: шлях -> кількість запитів 2xx
shlyahy_404 = defaultdict(set)       # ⭐3: ip -> множина різних шляхів з 404
vsi_ip = set()

with open("data/access.log", encoding="utf-8") as f:
    tekst = f.read()
    f.seek(0)
    for ryadok in f:
        m = shablon.search(ryadok)
        if not m:
            continue
        vsi_ip.add(m["ip"])
        if m["kod"].startswith("2"):
            uspishni[m["shlyah"]] += 1
        if m["kod"] == "404":
            shlyahy_404[m["ip"]].add(m["shlyah"])

# ⭐1
print("⭐1. Найпопулярніші шляхи серед успішних запитів (2xx)")
for shlyah, n in uspishni.most_common(3):
    print(f"   {n:>3}  {shlyah}")

# ⭐2: остання частина IP -> x. Групу (\d+\.\d+\.\d+\.) лишаємо, останнє число міняємо.
anonim = re.sub(r"(\d+\.\d+\.\d+\.)\d+", r"\1x", tekst)
with open("praktyka/06-regex-log/access_anonim.log", "w", encoding="utf-8", newline="\n") as out:
    out.write(anonim)
zalishky = re.findall(r"\d+\.\d+\.\d+\.\d+ ", anonim)
print("\n⭐2. Анонімізація: access_anonim.log записано")
print("   повних IP з пробілом після них у новому файлі:", zalishky)

# ⭐3
print("\n⭐3. IP, що отримали 404 на 2+ РІЗНИХ шляхів")
pidozrili = {ip: s for ip, s in shlyahy_404.items() if len(s) >= 2}
for ip, s in sorted(pidozrili.items(), key=lambda x: -len(x[1])):
    print(f"   {ip:<16} {len(s)}  {', '.join(sorted(s))}")
print("\n   Усі IP з 404 і кількість різних шляхів:")
for ip, s in sorted(shlyahy_404.items(), key=lambda x: -len(x[1])):
    print(f"   {ip:<16} {len(s)}  {', '.join(sorted(s))}")
