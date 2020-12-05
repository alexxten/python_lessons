import tkinter as tk

window = tk.Tk()
greeting_label = tk.Label(
    text='Hello, Ilya :)',
    background='gray',
    foreground='green',
    width=20,
    height=20,
)
greeting_label.pack()

tk.Button(width=20, height=50).pack()
# tk.Text()
# tk.Frame()
window.mainloop()