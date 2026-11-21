import tkinter as tk

vikno = tk.Tk()
vikno.title("Реєстрація — grid")

# Таблиця: рядки 0…6, стовпці 0 (підписи) і 1 (поля).
tk.Label(vikno, text="Реєстрація", font=("TkDefaultFont", 14, "bold")).grid(
    row=0, column=0, columnspan=2, pady=8)

POLIA = [("Імʼя:", ""), ("Пошта:", ""), ("Телефон:", ""), ("Пароль:", "•")]
for i, (pidpys, show) in enumerate(POLIA, start=1):
    tk.Label(vikno, text=pidpys).grid(row=i, column=0, sticky="e", padx=6, pady=3)
    tk.Entry(vikno, show=show).grid(row=i, column=1, sticky="ew", padx=6)

tk.Checkbutton(vikno, text="Погоджуюсь з умовами").grid(
    row=5, column=1, sticky="w", padx=6, pady=3)

knopky = tk.Frame(vikno)
knopky.grid(row=6, column=0, columnspan=2, sticky="e", padx=6, pady=8)
tk.Button(knopky, text="Скасувати").pack(side="right", padx=(6, 0))
tk.Button(knopky, text="Зареєструватись").pack(side="right")

# ⭐1: при розтягуванні тягнеться лише стовпець з полями
vikno.columnconfigure(1, weight=1)

vikno.mainloop()
