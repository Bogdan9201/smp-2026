import tkinter as tk

vikno = tk.Tk()
vikno.title("Реєстрація — place")
vikno.geometry("380x300")

tk.Label(vikno, text="Реєстрація", font=("TkDefaultFont", 14, "bold")).place(x=130, y=10)

POLIA = [("Імʼя:", ""), ("Пошта:", ""), ("Телефон:", ""), ("Пароль:", "•")]
for i, (pidpys, show) in enumerate(POLIA):
    y = 55 + i * 35
    tk.Label(vikno, text=pidpys, anchor="e", width=10).place(x=10, y=y)
    tk.Entry(vikno, show=show, width=26).place(x=110, y=y)

tk.Checkbutton(vikno, text="Погоджуюсь з умовами").place(x=105, y=200)

# кнопки притиснуті до правого нижнього кута: relx=1 + anchor="se"
tk.Button(vikno, text="Скасувати").place(relx=1.0, x=-10, rely=1.0, y=-10, anchor="se")
tk.Button(vikno, text="Зареєструватись").place(relx=1.0, x=-100, rely=1.0, y=-10, anchor="se")

vikno.mainloop()
