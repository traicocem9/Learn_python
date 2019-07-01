from tkinter import *
import datetime
import sys

def time_clock():
	time = str(datetime.datetime.now())[11:19]
	clock.config(text = time)
	clock.after(100, time_clock)
root = Tk()
root.title('Clock')
clock = Label(root, font =('time', 150, 'bold'), bg = "white",)
clock.grid(row = 0, column = 1)
time_clock()
root.mainloop()

