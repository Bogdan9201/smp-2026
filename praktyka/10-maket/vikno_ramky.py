import tkinter as tk

PIDKAZKY = {
    "Імʼя:": "Імʼя та прізвище, як у документі.",
    "Пошта:": "На цю адресу прийде лист із підтвердженням.",
    "Телефон:": "Формат: +380 XX XXX XX XX.",
    "Пароль:": "Щонайменше 8 символів; вводяться як «•».",
}
ZAHALNA = "Наведіть фокус на поле — тут зʼявиться підказка."

vikno = tk.Tk()
vikno.title("Реєстрація — вікно з рамками")
vikno.minsize(560, 300)

# --- смуга стану: пакуємо ПЕРШОЮ, щоб вона зайняла весь низ на всю ширину
stan = tk.Label(vikno, text="Готово", anchor="w", relief="sunken", bd=1, padx=6)
stan.pack(side="bottom", fill="x")

# --- ліворуч: форма (рамка з grid усередині)
forma = tk.Frame(vikno, padx=10, pady=10)
forma.pack(side="left", fill="both", expand=True)

# --- праворуч: панель «Підказка» (фіксована ширина, тягнеться лише по висоті)
panel = tk.LabelFrame(vikno, text="Підказка", padx=8, pady=8, width=200)
panel.pack(side="right", fill="y", padx=(0, 10), pady=10)
panel.pack_propagate(False)
tekst_pidkazky = tk.Label(panel, text=ZAHALNA, wraplength=170, justify="left", anchor="nw")
tekst_pidkazky.pack(fill="both", expand=True)


def pokazaty(pidpys):
    tekst_pidkazky.config(text=PIDKAZKY.get(pidpys, ZAHALNA))
    stan.config(text=f"Поле: {pidpys.rstrip(':')}")


tk.Label(forma, text="Реєстрація", font=("TkDefaultFont", 14, "bold")).grid(
    row=0, column=0, columnspan=2, pady=(0, 8))

for i, (pidpys, show) in enumerate(
        [("Імʼя:", ""), ("Пошта:", ""), ("Телефон:", ""), ("Пароль:", "•")], start=1):
    tk.Label(forma, text=pidpys).grid(row=i, column=0, sticky="e", padx=6, pady=3)
    pole = tk.Entry(forma, show=show)
    pole.grid(row=i, column=1, sticky="ew", padx=6)
    pole.bind("<FocusIn>", lambda e, p=pidpys: pokazaty(p))

tk.Checkbutton(forma, text="Погоджуюсь з умовами").grid(
    row=5, column=1, sticky="w", padx=6, pady=3)

knopky = tk.Frame(forma)
knopky.grid(row=6, column=0, columnspan=2, sticky="e", padx=6, pady=8)
tk.Button(knopky, text="Скасувати",
          command=lambda: stan.config(text="Скасовано")).pack(side="right", padx=(6, 0))
tk.Button(knopky, text="Зареєструватись",
          command=lambda: stan.config(text="Форму надіслано")).pack(side="right")

forma.columnconfigure(1, weight=1)

vikno.mainloop()
