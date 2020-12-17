from tkinter import *

window = Tk()
window.title("tkinter.LEFT, RIGHT, TOP, BOTTOM")
window.geometry("450x350")

button1 = Button(window, text="LEFT")
button1.pack(side=LEFT)

button2 = Button(window, text="RIGHT")
button2.pack(side=RIGHT)

button3 = Button(window, text="TOP")
button3.pack(side=TOP)

button4 = Button(window, text="BOTTOM")
button4.pack(side=BOTTOM)

window.mainloop()
