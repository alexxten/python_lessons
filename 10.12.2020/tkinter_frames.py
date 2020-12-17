from tkinter import *

window = Tk()
window.geometry("400x300")

frame1 = Frame(window, width=200, height=150, background="Blue")
frame1.grid(row=0, column=0)

frame2 = Frame(window, width=200, height=150, background="Red")
frame2.grid(row=1, column=0)

frame3 = Frame(window, width=200, height=150, background="Green")
frame3.grid(row=0, column=1)

frame4 = Frame(window, width=200, height=150, background="Yellow")
frame4.grid(row=1, column=1)

window.mainloop()
