from tkinter import *
root=Tk()

Label(root,text="Username").grid(row=0,column=0)
Label(root,text="Password").grid(row=1,column=0)

Entry(root).grid(row=0,column=1)
Entry(root).grid(row=1,column=1)

root.mainloop()