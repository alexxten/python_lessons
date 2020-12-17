import tkinter as tk
from tkinter import ttk


def change_bg(event: str) -> None:
    color = combobox.get()
    root['bg'] = color


root = tk.Tk()

l = tk.Label(text='Выберите цвет', font=("Courier", 14))
l.grid(column=0, ipady=10, ipadx=10, padx=10, pady=10)

combobox = ttk.Combobox(root, values=['grey', 'red', 'black'], font=("Courier", 12))
combobox.grid(column=0, row=1, padx=10, pady=10)

btn = tk.Button(text='Тык по кнопе', bg='lightgreen', font=("Courier", 10))
btn.grid(column=0, row=4, padx=10, pady=10)
btn.bind('<Button-1>', change_bg)

root.geometry("300x200")
root.mainloop()
