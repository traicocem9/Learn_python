from tkinter import *
from tkinter import filedialog

root = Tk()
canvas = Canvas(root, width = 500 , height = 600)
canvas.pack()


frame_1 = Frame(root, bg = '#99ccff')
frame_1.place(relx = 0.1, rely = 0.05, relwidth = 0.8, relheight = 0.2)

frame_2 = Frame(root, bg = '#99ccff')
frame_2.place(relx = 0.1, rely = 0.3, relwidth = 0.8, relheight = 0.6 )

def openfile():
    root_filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    print(root_filename)
    label['text'] = root_filename
    text['text'] = open(root_filename).read()
button = Button(frame_1, text = 'open file',activeforeground = "red", command = lambda : openfile())
button.place(relx = 0.05, rely = 0.1, anchor = 'nw', relwidth = 0.9, relheight = 0.2)

label = Label(frame_1)
label.place(relx = 0.05, rely = 0.4, relwidth = 0.9, relheight = 0.5)

text = Text(frame_2)
text.place(relx = 0.05, rely = 0.05, relwidth = 0.9, relheight = 0.9,)

root.mainloop()