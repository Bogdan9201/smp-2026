import argparse
import re
from datetime import datetime
from pathlib import Path

# 6. міні-мова командного рядка: --papka, --top, --shablon
parser = argparse.ArgumentParser(
    description="Звіт про найбільші файли в теці: імʼя, розмір у КБ, дата зміни.",
    usage="%(prog)s [ПАПКА] [--papka ПАПКА] [--top N] [--shablon ШАБЛОН] [-h]",
    add_help=False,
)
parser._positionals.title = "позиційні аргументи"
parser._optionals.title = "параметри"
parser.add_argument("papka_pozytsiino", nargs="?", metavar="ПАПКА",
                    help="тека (можна й без --papka)")
parser.add_argument("--papka", default=None,
                    help="тека для звіту (за замовчуванням — поточна)")
parser.add_argument("--top", type=int, default=10, metavar="N",
                    help="скільки найбільших файлів показати (за замовчуванням 10)")
parser.add_argument("--shablon", default="*",
                    help='glob-шаблон імен, наприклад "*.txt" (за замовчуванням "*")')
parser.add_argument("-h", "--help", action="help",
                    help="показати цю довідку й вийти")
args = parser.parse_args()

PAPKA = Path(args.papka or args.papka_pozytsiino or ".")

# 1. glob
fayly = [f for f in PAPKA.glob(args.shablon) if f.is_file()]
fayly.sort(key=lambda f: f.stat().st_size, reverse=True)

# 2. зріз
top = fayly[:args.top]

print(f"{'Імʼя':<30}{'КБ':>8}  Змінено")
for f in top:
    kb = f.stat().st_size / 1024
    zmineno = datetime.fromtimestamp(f.stat().st_mtime)
    # 3. формат рядків і 4. формат дати
    print(f"{f.name:<30}{kb:>8.1f}  {zmineno:%d.%m.%Y}")

# 5. регулярний вираз
z_datoyu = [f for f in fayly if re.search(r"\d{4}-\d{2}-\d{2}", f.name)]
print(f"\nЗ датою в назві: {len(z_datoyu)}")
