from tkinter import *
root = Tk()
root.title("Calculater")
root.geometry("500x430")

eqution = StringVar()


eqStr = ""
def calculater(event):
    global eqStr
    char = event.widget.cget("text")
    if char == "=":
        answer = eval(eqution.get())
        eqution.set(answer)
    else:
        eqStr = eqStr + char
        eqution.set(eqStr)


entry = Entry(root,font=("Arial",30),relief=RAISED,borderwidth=8,background="red",textvariable=eqution)
entry.grid(row=0,column=0,columnspan=4)

button = Button(root,text = "7", font=("Arial",30),height=1,width=4,relief=RAISED,borderwidth=8,background="yellow")
button.grid(row=1,column=0)
button.bind("<Button-1>",calculater)


button = Button(root,text = "8", font=("Arial",30),height=1,width=4,relief=RAISED,borderwidth=8,background="yellow")
button.grid(row=1,column=1)
button.bind("<Button-1>",calculater)


button = Button(root,text = "9", font=("Arial",30),height=1,width=4,relief=RAISED,borderwidth=8,background="yellow")
button.grid(row=1,column=2)
button.bind("<Button-1>",calculater)
button.bind("<Button-1>",calculater)


button = Button(root,text = "+", font=("Arial",30),height=1,width=4,relief=RAISED,borderwidth=8,background="yellow")
button.grid(row=1,column=3)
button.bind("<Button-1>",calculater)


#---------------------
button = Button(root,text = "4", font=("Arial",30),height=1,width=4,relief=RAISED,borderwidth=8,background="yellow")
button.grid(row=2,column=0)
button.bind("<Button-1>",calculater)

button = Button(root,text = "5", font=("Arial",30),height=1,width=4,relief=RAISED,borderwidth=8,background="yellow")
button.grid(row=2,column=1)
button.bind("<Button-1>",calculater)

button = Button(root,text = "6", font=("Arial",30),height=1,width=4,relief=RAISED,borderwidth=8,background="yellow")
button.grid(row=2,column=2)
button.bind("<Button-1>",calculater)

button = Button(root,text = "-", font=("Arial",30),height=1,width=4,relief=RAISED,borderwidth=8,background="yellow")
button.grid(row=2,column=3)
button.bind("<Button-1>",calculater)

#-----------------------
button = Button(root,text = "1", font=("Arial",30),height=1,width=4,relief=RAISED,borderwidth=8,background="yellow")
button.grid(row=3,column=0)
button.bind("<Button-1>",calculater)

button = Button(root,text = "2", font=("Arial",30),height=1,width=4,relief=RAISED,borderwidth=8,background="yellow")
button.grid(row=3,column=1)
button.bind("<Button-1>",calculater)

button = Button(root,text = "3", font=("Arial",30),height=1,width=4,relief=RAISED,borderwidth=8,background="yellow")
button.grid(row=3,column=2)
button.bind("<Button-1>",calculater)

button = Button(root,text = "*", font=("Arial",30),height=1,width=4,relief=RAISED,borderwidth=8,background="yellow")
button.grid(row=3,column=3)
button.bind("<Button-1>",calculater)

#---------------------

button = Button(root,text = ".", font=("Arial",30),height=1,width=4,relief=RAISED,borderwidth=8,background="yellow")
button.grid(row=4,column=0)
button.bind("<Button-1>",calculater)

button = Button(root,text = "0", font=("Arial",30),height=1,width=4,relief=RAISED,borderwidth=8,background="yellow")
button.grid(row=4,column=1)
button.bind("<Button-1>",calculater)

button = Button(root,text = "/", font=("Arial",30),height=1,width=4,relief=RAISED,borderwidth=8,background="yellow")
button.grid(row=4,column=2)
button.bind("<Button-1>",calculater)

button = Button(root,text = "=", font=("Arial",30),height=1,width=4,relief=RAISED,borderwidth=8,background="yellow")
button.grid(row=4,column=3)
button.bind("<Button-1>",calculater)













root.mainloop()