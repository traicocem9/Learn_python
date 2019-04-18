from tkinter import *
from tkinter import filedialog

root = Tk()

canvas = Canvas(root, width = 500 , height = 600)
canvas.pack()
# create bule frame in root
frame_1 = Frame(root, bg = '#99ccff')
frame_1.place(relx = 0.1, rely = 0.05, relwidth = 0.8, relheight = 0.2)

def Openfile(root):
    root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

button = Button(frame_1, text = 'open file',activeforeground = "red", command = quit )
button.place(relx = 0.05, rely = 0.1, anchor = 'nw', relwidth = 0.9, relheight = 0.2)

label = Label(frame_1)
label.place(relx = 0.05, rely = 0.4, relwidth = 0.9, relheight = 0.5)

root.mainloop()