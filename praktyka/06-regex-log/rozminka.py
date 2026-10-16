import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

with open("data/words.txt", encoding="utf-8") as f:
    for ryadok in f:
        print(ryadok.rstrip().upper())

suma = 0.0
kilkist = 0
with open("data/mbox-short.txt", encoding="utf-8") as f:
    for ryadok in f:
        if ryadok.startswith("X-DSPAM-Confidence:"):
            suma += float(ryadok.split(":")[1])
            kilkist += 1

print()
print(f"Рядків X-DSPAM-Confidence: {kilkist}")
print(f"Середнє: {suma / kilkist}")
