import tkinter as tk

vikno = tk.Tk()
vikno.title("Реєстрація — pack")

tk.Label(vikno, text="Реєстрація", font=("TkDefaultFont", 14, "bold")).pack(pady=8)

POLIA = [("Імʼя:", ""), ("Пошта:", ""), ("Телефон:", ""), ("Пароль:", "•")]
for pidpys, show in POLIA:
    ryadok = tk.Frame(vikno)
    ryadok.pack(fill="x", padx=10, pady=2)
    tk.Label(ryadok, text=pidpys, width=10, anchor="e").pack(side="left")
    tk.Entry(ryadok, show=show).pack(side="left", fill="x", expand=True)

# прапорець: рамка з відступом, що дорівнює ширині підпису
ryadok = tk.Frame(vikno)
ryadok.pack(fill="x", padx=10, pady=2)
tk.Label(ryadok, width=10).pack(side="left")
tk.Checkbutton(ryadok, text="Погоджуюсь з умовами").pack(side="left")

knopky = tk.Frame(vikno)
knopky.pack(fill="x", padx=10, pady=8)
tk.Button(knopky, text="Скасувати").pack(side="right", padx=(6, 0))
tk.Button(knopky, text="Зареєструватись").pack(side="right")

vikno.mainloop()
