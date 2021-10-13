from tkinter import *
root=Tk()

class demo:
	"""docstring for Demo"""
	def __init__(self, rootone):
		frame=Frame(rootone)
		frame.pack()
		self.p=Button(frame,text="Hai Ankit",command=self.prntmsg)
		self.p.pack()
		Button(frame,text="Exit",command=frame.quit).pack()

	def prntmsg(self):
		print("Welcome Ankit")	

obj=demo(root)

root.mainloop()