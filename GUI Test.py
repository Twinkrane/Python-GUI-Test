from tkinter import *

root = Tk()
root.title("Тест GUI")
root.geometry("400x250+300+250")
root.resizable(width=False, height=False)


btnN = Button(text="СЕВЕР", bg="#0008FF", fg="#FFFFFF", pady="2", font="12", width=12)
btnN.pack(side=TOP)
btnS = Button(text="ЮГ", bg="#FF0404", fg="#FFFFFF",  pady="2", font="12", width=12)
btnS.pack(side=BOTTOM)
btnW = Button(text="ЗАПАД", bg="#000000", fg="#FFFFFF",  pady="2", font="12", width=12)
btnW.pack(side=LEFT)
btnE = Button(text="ВОСТОК", bg="#0C9002", fg="#FFFFFF",  pady="2", font="12", width=12)
btnE.pack(side=RIGHT)
label = Label(text="Куда идти?", font="12", pady="80")
label.pack()

root.mainloop()