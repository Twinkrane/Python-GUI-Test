from tkinter import *

root = Tk()
root.title("Метод place")
root.geometry("400x250")
root.resizable(width=False, height=False)


def medved():
    puch = '\n\n' + 'Пух'
    text.insert(END, puch)


def ptitsa():
    sova = '\n\n' + 'Сова'
    text.insert(END, sova)


puch = Button(text="Puch", background="#483D8B", foreground="#fff",
              width=12, command=medved).place(x=50, y=200)
sova = Button(text="Sova", background="#483D8B", foreground="#fff",
              width=12, command=ptitsa).place(x=250, y=200)

text = Text(width=47, height=10, bg="#F8F8FF", fg='black', wrap=WORD)
text.place(x=10, y=10)

root.mainloop()
