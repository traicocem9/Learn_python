from tkinter import *
import random 
import time

width = 500.0
height = 500.0

root = Tk()

root.title('Bounce!')
root.resizable(0,0)
root.wm_attributes('-topmost', 1)

canvas = Canvas(root, width = width, height = height)
canvas.pack()
root.update()

class ball:
    def __init__(self, canvas, color, player):
        self.canvas = canvas
        self.player = player
        self.ball = canvas.create_oval(10,10,25,25, fill=color)        
        self.canvas.move(self.ball,245 ,100)
        X = [-3,-2,1,0,1,2,3]
        random.shuffle(X)
        self.x = X[0]
        self.y = -2
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()

    def hit(self, pos):
        player_pos = self.canvas.coords(self.player.player)
        if pos[2] >= player_pos[0] and pos[0] <= player_pos[2]:
            if pos[3] >= player_pos[1] and pos[1] <= player_pos[3]:
                return True
            return False



    def draw(self):
        self.canvas.move(self.ball,self.x,self.y)
        pos = self.canvas.coords(self.ball)       
        if pos[1] <= 0:
            self.y = 2
        if pos[3] >= self.canvas_height:
            self.y = -2
        
        if pos[0] <= 0:
            self.x = 2
        if pos[2] >= self.canvas_width:
            self.x = -2
        if self.hit(pos) == True:
            self.y = -2

class player:
    def __init__(self, canvas):
        self.canvas = canvas
        self.player = canvas.create_rectangle(0,0,100,10, fill = "blue")
        self.canvas.move(self.player, 245,300)
        self.x = 2
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
    def draw(self):
        self.canvas.move(self.player, self.x, 0)
        pos_p = self.canvas.coords(self.player)
        print (pos_p)
        if pos_p[0] <= 0:
            self.x = 2
        if pos_p[2] >= self.canvas_width:
            self.x = -2
    def turn_left(self, evt):
            self.x = -2
    def turn_right(self, evt):
            self.x = 2

player = player(canvas)      
ball = ball(canvas, "red", player)

while 1:
    ball.draw()
    player.draw()
    root.update_idletasks()
    root.update()
    time.sleep(0.01)
