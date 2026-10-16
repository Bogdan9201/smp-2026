import re
import sys
import time

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass


def zamir(shablon, tekst):
    start = time.perf_counter()
    re.match(shablon, tekst)
    return time.perf_counter() - start


print("n    час, с      відношення до попереднього")
poperednie = None
for n in range(16, 27):
    t = zamir(r"(a+)+$", "a" * n + "X")
    vidnoshennia = f"{t / poperednie:.2f}" if poperednie else "-"
    print(f"{n:<4} {t:<11.5f} {vidnoshennia}")
    poperednie = t

print("\nВиправлення на 100 000 літер:")
tekst = "a" * 100_000 + "X"
print(f"  a+$           : {zamir(r'a+$', tekst):.5f} с   (прибрали вкладений квантифікатор)")
if sys.version_info >= (3, 11):
    print(f"  (?>a+)+$      : {zamir(r'(?>a+)+$', tekst):.5f} с   (атомарна група)")
else:
    print("  (?>…) потребує Python 3.11+")
print(f"  (?=(a+))\\1 ...: {zamir(r'(?=(a+))\\1$', tekst):.5f} с   (lookahead + зворотне посилання імітує атомарність)")
