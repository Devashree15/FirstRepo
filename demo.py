from tkinter import *
from tkinter import messagebox
import winsound
root=Tk()

root.title("msgbox")
root.geometry("200x200")

#loop


def caller():
    i=0
    while i<50:
        a=messagebox.askquestion("I see you","I told  ya not to click on me 👀")
        if a=="yes":
            messagebox.askquestion("i told ya!","😈")
        elif a=="no":
            messagebox.askquestion("nope not gonna go out of here","💀")
        else:
            print("none")
        i=i+1
        winsound.Beep(800, 200)




b1=Button(root,text="Don't you dare click on me!",command=caller).pack()
root.mainloop()


