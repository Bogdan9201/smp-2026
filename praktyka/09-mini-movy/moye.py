import re

SPEC = re.compile(
    r"""^
    (?:(?P<fill>.)?(?P<align>[<>^]))?   # [заповнювач]вирівнювання
    (?P<zero>0)?                        # прапорець 0: доповнення нулями
    (?P<width>\d+)?                     # ширина
    (?:\.(?P<prec>\d+))?                # .точність
    (?P<type>f)                         # тип (обов'язковий: без нього format діє як 'g')
    $""",
    re.VERBOSE | re.DOTALL,
)


def moye(chyslo, spec):
    m = SPEC.match(spec)
    if m is None:
        raise ValueError(f"Невідома специфікація: {spec!r}")

    fill = m["fill"]
    align = m["align"]
    zero = m["zero"] is not None
    width = int(m["width"]) if m["width"] else 0
    # без точності в типі f Python дає 6 знаків
    prec = int(m["prec"]) if m["prec"] is not None else 6

    # округлення — вбудованим f-рядком (за умовою завдання)
    tilo = f"{chyslo:.{prec}f}"

    # прапорець 0 без явного вирівнювання: нулі між знаком і цифрами
    if zero and align is None:
        znak = ""
        if tilo[0] in "+-":
            znak, tilo = tilo[0], tilo[1:]
        return znak + tilo.rjust(width - len(znak), "0")

    # прапорець 0 разом із явним вирівнюванням: заповнювач за замовчуванням '0'
    if zero and fill is None:
        fill = "0"
    fill = fill or " "
    align = align or ">"          # числа за замовчуванням вирівнюються праворуч

    pad = max(width - len(tilo), 0)
    if align == "<":
        return tilo + fill * pad
    if align == ">":
        return fill * pad + tilo
    liva = pad // 2               # зайвий символ при центруванні — праворуч
    return fill * liva + tilo + fill * (pad - liva)


if __name__ == "__main__":
    vypadky = [
        (3.14159, ".2f"), (3.14159, "8.2f"), (3.14159, "<8.2f"),
        (3.14159, "^8.2f"), (3.14159, "*>10.3f"), (2.5, ".0f"),
        (42.0, "06.1f"), (1234.5, "_^12.1f"), (7.0, "f"),
        (0.1, ".20f"), (-1.5, ">7.1f"), (99.999, ".2f"),
    ]
    vse_dobre = True
    for x, s in vypadky:
        moje, etalon = moye(x, s), format(x, s)
        znak = "✅" if moje == etalon else "❌"
        vse_dobre &= moje == etalon
        print(f"{znak} moye({x}, {s!r:10}) = {moje!r:22} format = {etalon!r}")
    print("\nУсі 12 збіглися" if vse_dobre else "\nЄ розбіжності")
