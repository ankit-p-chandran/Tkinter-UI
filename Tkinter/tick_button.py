from tkinter import *
root=Tk()

def fun():
	print("Hai Ankit")
def cancel():
	print("Tick Cancel")	

f=Frame(root).pack()
Button(f,text="Login",command=fun).pack()
Button(f,text="Cancel",command=cancel).pack()
root.mainloop()