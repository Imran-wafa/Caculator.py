from tkinter import *

root = Tk()
root.title("caculator")
e = Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=10,padx=10,pady=10)
def button_add():
	num1=e.get()
	global fnum
	fnum = int(num1)
	e.delete(0,'end')
def button_equal():
	e.delete(0,'end')
	num2= e.get()
	global snum
	snum = int(num2)
	e.insert(0,fnum+snum)
def button_clear():
	e.delete(0,'end')
def button_click(number):
	e.insert("end",number)
b1 = Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1))
b2 = Button(root,text="2",padx=40,pady=20,command=lambda: button_click(2))
b3 = Button(root,text="3",padx=40,pady=20,command=lambda: button_click(3))
b4 = Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4))
b5 = Button(root,text="5",padx=40,pady=20,command=lambda: button_click(5))
b6 = Button(root,text="6",padx=40,pady=20,command=lambda: button_click(6))
b7 = Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7))
b8 = Button(root,text="8",padx=40,pady=20,command=lambda: button_click(8))
b9 = Button(root,text="9",padx=40,pady=20,command=lambda: button_click(9))
b0 = Button(root,text="0",padx=40,pady=20,command=lambda: button_click(0))
bclear = Button(root,text="Clear",padx=79,pady=20,command=button_clear)
bequal = Button(root,text="=",padx=91,pady=20,command=button_equal)
badd = Button(root,text="+",padx=39,pady=20,command=button_add)
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)

b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)

b0.grid(row=4,column=0)
bequal.grid(row=4,column=1,columnspan=2)
bclear.grid(row=5,column=0,columnspan=2)
badd.grid(row=5,column=2)
root.mainloop()
