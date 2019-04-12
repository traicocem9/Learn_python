from tkinter import *
import random 
import time

width = 500
height = 500

root = Tk()

root.title('Bounce!')
root.resizable(0,0)
root.wm_attributes('-topmost', 1)

canvas = Canvas(root, width = width, height = height)
canvas.pack()
root.update()

class ball():
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.ball = canvas.create_oval(10,10,25,25, fill=color)        
        self.canvas.move(self.ball,245 ,100)
        X = [-3,-2,1,0,1,2,3]
        random.shuffle(X)
        self.x = X[0]
        self.y = -2
        self.canvas.width = self.canvas.winfo_width()
        self.canvas.height = self.canvas.winfo_height()

    def draw(self):
        self.canvas.move(self.ball,self.x,self.y)
        pos = self.canvas.coords(self.ball)       
        if pos[1] <= 0:
            self.y = 2
        if pos[3] >= self.canvas.height:
            self.y = 0
            self.x = 0
        if pos[0] <= 0:
            self.x = 2
        if pos[2] >= self.canvas.width:
            self.x = -2
        

class player:
    def __init__(self, canvas):
        self.canvas = canvas
        self.player = canvas.create_rectangle(0,0,100,10, fill = "blue")
        self.canvas.move(self.player, 245,300)


ball = ball(canvas, "red")
player = player(canvas)
while 1:
    ball.draw()
    root.update_idletasks()
    root.update()
    time.sleep(0.01)
