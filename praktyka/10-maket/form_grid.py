import tkinter as tk

PIDPYSY = {
    "uk": {
        "vikno": "Реєстрація — grid",
        "zaholovok": "Реєстрація",
        "imia": "Імʼя:",
        "poshta": "Пошта:",
        "telefon": "Телефон:",
        "parol": "Пароль:",
        "umovy": "Погоджуюсь з умовами",
        "ok": "Зареєструватись",
        "skasuvaty": "Скасувати",
    },
    "de": {
        "vikno": "Registrierung — grid",
        "zaholovok": "Registrierung",
        "imia": "Vor- und Nachname:",
        "poshta": "E-Mail-Adresse:",
        "telefon": "Telefonnummer:",
        "parol": "Passwort:",
        "umovy": "Ich stimme den Bedingungen zu",
        "ok": "Registrieren",
        "skasuvaty": "Abbrechen",
    },
}
MOVA = "uk"          # змініть на "de" — макет лишається тим самим
T = PIDPYSY[MOVA]

vikno = tk.Tk()
vikno.title(T["vikno"])

# Таблиця: рядки 0…6, стовпці 0 (підписи) і 1 (поля).
tk.Label(vikno, text=T["zaholovok"], font=("TkDefaultFont", 14, "bold")).grid(
    row=0, column=0, columnspan=2, pady=8)

POLIA = [(T["imia"], ""), (T["poshta"], ""), (T["telefon"], ""), (T["parol"], "•")]
for i, (pidpys, show) in enumerate(POLIA, start=1):
    tk.Label(vikno, text=pidpys).grid(row=i, column=0, sticky="e", padx=6, pady=3)
    tk.Entry(vikno, show=show).grid(row=i, column=1, sticky="ew", padx=6)

tk.Checkbutton(vikno, text=T["umovy"]).grid(row=5, column=1, sticky="w", padx=6, pady=3)

knopky = tk.Frame(vikno)
knopky.grid(row=6, column=0, columnspan=2, sticky="e", padx=6, pady=8)
tk.Button(knopky, text=T["skasuvaty"]).pack(side="right", padx=(6, 0))
tk.Button(knopky, text=T["ok"]).pack(side="right")

# ⭐1: при розтягуванні тягнеться лише стовпець з полями, підписи — ні
vikno.columnconfigure(1, weight=1)

vikno.mainloop()
