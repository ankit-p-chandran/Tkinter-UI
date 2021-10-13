from tkinter import *

root=Tk()

def save():
	print("Save")
def redo():
	print("Redo")
def undo():
	print("Undo")		

mymenu=Menu(root)
root.config(menu=mymenu)

submenu= Menu(mymenu)

mymenu.add_cascade(label="File",menu=submenu)
submenu.add_command(label="Save",command=save)

submenu.add_separator()
submenu.add_command(label="exit",command=root.quit)

newmenu= Menu(mymenu)

mymenu.add_cascade(label="Edit",menu=newmenu)
newmenu.add_command(label="Undo",command=undo)

newmenu.add_separator()
newmenu.add_command(label="Redo",command=redo)

root.mainloop()