from tkinter import *
import tkinter.messagebox
root=Tk()

tkinter.messagebox.showinfo("Message","this is a message")
tkinter.messagebox.showwarning("Warning","this is a warning")
tkinter.messagebox.showerror("Error","this is a error")
tkinter.messagebox.askquestion("Question","You want to save")
tkinter.messagebox.askokcancel("Question","You want to save")
tkinter.messagebox.askyesno("Question","You want to save")
tkinter.messagebox.askretrycancel("Question","You want to save")

root.mainloop()