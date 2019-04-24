from tkinter import *


root = Tk()
canvas = Canvas(root, width = 1600, height =800)
canvas.pack()


frame_1 = Frame(root, bg = '#ffa64d')
frame_1.place(relx = 0.001,rely = 0.13, relwidth = 0.55, relheight = 1)


frame_2 = Frame(root, bg = '#ffa64d')
frame_2.place(relx = 0.7, rely = 0.13, relwidth = 0.3, relheight = 1)

title = Label(root, font = ('arial', 39, 'bold' ),text= 'phần mềm tính tiền')
title.place(relx = 0.1, rely = 0, relwidth = 0.8, relheight = 0.1)
title_2 = Label(root, font = ('arial', 10, 'bold'),text = 'Made by traicocem')
title_2.place(relx = 0.3, rely = 0.1 , relwidth = 0.3, relheight = 0.02)

bg_cl = '#ffa64d'
#------------------------------------------------------------_VAR_-------------------------------------------#
varT = StringVar()
varP = StringVar()
varC = StringVar()
var3 = StringVar()
varCHOCO = StringVar()
varChese = StringVar()
var3H = StringVar()
varPudding = StringVar()
varMint = StringVar()
varRoy = StringVar()

varT.set('0')
varP.set('0')
varC.set('0')
var3.set('0')
varCHOCO.set('0')
varChese.set('0')
var3H.set('0')
varPudding.set('0')
varMint.set('0')
varRoy.set('0')

#Stick
Stick_x = Label(frame_1, bg = 'black')
Stick_x.place(relx = 0, rely = 0.06, relwidth = 11, relheight = 0.005)

Stick_y = Label(frame_1, bg = 'black')
Stick_y.place(relx = 0.28, rely = 0,relwidth = 0.005, relheight = 100 )
#frame_1_title
fg = '#4d4dff'
font_1 = ('Helvetica', 20,'bold')

#item
font_2 = ('arial', 15, )
font_2_eng = ('arial', 10,'italic')

#SL
font_3 = ('arial', 15)


def item():
    

    it_1 = Label(frame_1, font = font_2,text = 'Trà sữa',bg = bg_cl)
    it_1.place(relx = 0.011, rely = 0.08, relwidth = 0.18, relheight = 0.05)
    it_1_e = Label(frame_1, font = font_2_eng,text = '_Milk Tea_',bg = bg_cl)
    it_1_e.place(relx = 0.06, rely = 0.12, relwidth = 0.08, relheight = 0.03)

    it_2 = Label(frame_1, font = font_2,text = 'Trà sữa panda',bg = bg_cl)
    it_2.place(relx = 0.011, rely = 0.16, relwidth = 0.18, relheight = 0.05)
    it_2_e = Label(frame_1, font = font_2_eng,text = '_Panda Milk Tea_',bg = bg_cl)
    it_2_e.place(relx = 0.012, rely = 0.20, relwidth = 0.18, relheight = 0.03)

    it_3 = Label(frame_1, font = font_2,text = 'Trà sữa coffee',bg = bg_cl)
    it_3.place(relx = 0.011, rely = 0.24, relwidth = 0.18, relheight = 0.05)
    it_3_e = Label(frame_1, font = font_2_eng,text = '_Coffee Milk Tea_',bg = bg_cl)
    it_3_e.place(relx = 0.012, rely = 0.28, relwidth = 0.18, relheight = 0.03)

    it_4 = Label(frame_1, font = font_2,text = 'Trà sữa 3Q',bg =bg_cl)
    it_4.place(relx = 0.011, rely = 0.32, relwidth = 0.18, relheight = 0.05)
    it_4_e = Label(frame_1, font = font_2_eng,text = '_3Q Milk Tea_',bg = bg_cl)
    it_4_e.place(relx = 0.012, rely = 0.36, relwidth = 0.18, relheight = 0.03)

    it_5 = Label(frame_1, font = font_2,text = 'Trà sữa socola',bg = bg_cl )
    it_5.place(relx = 0.011, rely = 0.40, relwidth = 0.18, relheight = 0.05)
    it_5_e = Label(frame_1, font = font_2_eng,text = '_Chocolate Milk Tea_',bg = bg_cl)
    it_5_e.place(relx = 0.012, rely = 0.44, relwidth = 0.18, relheight = 0.03)

    it_6 = Label(frame_1, font =font_2,text = 'Trà sữa phô mai',bg = bg_cl )
    it_6.place(relx = 0.011, rely = 0.48, relwidth = 0.18, relheight = 0.05)
    it_6_e = Label(frame_1, font = font_2_eng,text = '_Cheese Milk Tea_',bg = bg_cl)
    it_6_e.place(relx = 0.012, rely = 0.52, relwidth = 0.18, relheight = 0.03)

    it_7 = Label(frame_1, font = font_2,text = 'Trà sữa 3 anh em',bg = bg_cl)
    it_7.place(relx = 0.011, rely = 0.56, relwidth = 0.18, relheight = 0.05)
    it_7_e = Label(frame_1, font = font_2_eng,text = "_Three Hero's Milk Tea_",bg = bg_cl)
    it_7_e.place(relx = 0.012, rely = 0.60, relwidth = 0.18, relheight = 0.03)

    it_8 = Label(frame_1, font = font_2,text = 'Trà sữa bánh flan',bg = bg_cl )
    it_8.place(relx = 0.011, rely = 0.64, relwidth = 0.18, relheight = 0.05)
    it_8_e = Label(frame_1, font = font_2_eng,text = '_Pudding Milk Tea_',bg = bg_cl)
    it_8_e.place(relx = 0.012, rely = 0.68, relwidth = 0.18, relheight = 0.03)
    
    it_9 = Label(frame_1, font = font_2,text = 'Trà sữa bạc hà',bg = bg_cl)
    it_9.place(relx = 0.011, rely = 0.72, relwidth = 0.18, relheight = 0.05)
    it_9_e = Label(frame_1, font = font_2_eng,text = '_Mint Milk Tea_',bg = bg_cl)
    it_9_e.place(relx = 0.012, rely = 0.76, relwidth = 0.18, relheight = 0.03)

    it_10 = Label(frame_1, font = font_2,text = 'Trà sữa hoàng gia',bg = bg_cl)
    it_10.place(relx = 0.011, rely = 0.80, relwidth = 0.18, relheight = 0.05)
    it_10_e = Label(frame_1, font = font_2_eng,text = '_Royal Milk Tea_',bg = bg_cl)
    it_10_e.place(relx = 0.012, rely = 0.84, relwidth =0.18, relheight = 0.03)

def frame_1_title():
    Trà_sữa = Label(frame_1, font = font_1,text = 'Milk Tea',fg = fg, bg = bg_cl )
    Trà_sữa.place(relx = 0.011, rely = 0.01, relwidth = 0.18, relheight = 0.05)

    Giá_thành = Label(frame_1, font = font_1,text = 'Trà trái cây',fg = fg,bg = bg_cl)
    Giá_thành.place(relx = 0.3, rely = 0.01, relwidth = 0.18, relheight = 0.05)

    SL = Label(frame_1, font = font_1,text = 'smoothie',bd = 7 ,fg = fg, bg = bg_cl)
    SL.place(relx = 0.55, rely = 0.01, relwidth = 0.05, relheight = 0.05)

    Tổng_giá = Label(frame_1, font = font_1,text = 'Special Drink',fg = fg,bg = bg_cl )
    Tổng_giá.place(relx = 0.78, rely = 0.01, relwidth = 0.18, relheight = 0.05)

def Giá_thành():
    

    it_1 = Label(frame_1, font = font_2,text = 'Trà sữa',bg = bg_cl)
    it_1.place(relx = 0.3, rely = 0.08, relwidth = 0.18, relheight = 0.05)

    coffeesua = Text(frame_1, font = ('Helvetica', 20),bd =7)
    coffeesua.place(relx = 0.3, rely = 0.16, relwidth = 0.18, relheight = 0.05)

    cacao_nong = Text(frame_1, font = ('Helvetica', 20),bd =7)
    cacao_nong.place(relx = 0.3, rely = 0.24, relwidth = 0.18, relheight = 0.05)

    cacao_da = Text(frame_1, font = ('Helvetica', 20),bd =7)
    cacao_da.place(relx = 0.3, rely = 0.32, relwidth = 0.18, relheight = 0.05)

    Sinh_to = Text(frame_1, font = ('Helvetica', 20),bd =7)
    Sinh_to.place(relx = 0.3, rely = 0.40, relwidth = 0.18, relheight = 0.05)

    Tra_dao = Text(frame_1, font = ('Helvetica', 20),bd =7)
    Tra_dao.place(relx = 0.3, rely = 0.48, relwidth = 0.18, relheight = 0.05)

    Nuoc_ngot = Text(frame_1, font = ('Helvetica', 20),bd = 7)
    Nuoc_ngot.place(relx = 0.3, rely = 0.56, relwidth = 0.18, relheight = 0.05)

    Nuoc_suoi = Text(frame_1, font = ('Helvetica', 20),bd =7)
    Nuoc_suoi.place(relx = 0.3, rely = 0.64, relwidth = 0.18, relheight = 0.05)

    Dua_tuoi = Text(frame_1, font = ('Helvetica', 20),bd =5)
    Dua_tuoi.place(relx = 0.3, rely = 0.72, relwidth = 0.18, relheight = 0.05)

    Tra_da = Text(frame_1, font = ('Helvetica', 20),bd =7)
    Tra_da.place(relx = 0.3, rely = 0.80, relwidth = 0.18, relheight = 0.05)

def SL():
    
    
    sl1 = Entry(frame_1, font = font_3, textvariable = varT)
    sl1.place(relx = 0.22, rely = 0.09, relwidth = 0.05, relheight = 0.04)
    
    sl2 = Entry(frame_1, font = font_3, textvariable = varP)
    sl2.place(relx = 0.22, rely = 0.16, relwidth = 0.05, relheight = 0.04)

    sl3 = Entry(frame_1, font = font_3, textvariable = varC)
    sl3.place(relx = 0.22, rely = 0.24, relwidth = 0.05, relheight = 0.04)

    sl4 = Entry(frame_1, font = font_3, textvariable =var3)
    sl4.place(relx = 0.22, rely = 0.32, relwidth = 0.05, relheight = 0.04)

    sl5 = Entry(frame_1, font = font_3, textvariable =varCHOCO)
    sl5.place(relx = 0.22, rely = 0.40, relwidth = 0.05, relheight = 0.04)

    sl6 = Entry(frame_1, font = font_3, textvariable = varChese)
    sl6.place(relx = 0.22, rely = 0.48, relwidth = 0.05, relheight = 0.04)

    sl7 = Entry(frame_1, font =font_3, textvariable =var3H)
    sl7.place(relx = 0.22, rely = 0.56, relwidth = 0.05, relheight = 0.04)

    sl8 = Entry(frame_1, font = font_3, textvariable =varPudding)
    sl8.place(relx = 0.22, rely = 0.64, relwidth = 0.05, relheight = 0.04)

    sl9 = Entry(frame_1, font = font_3 , textvariable =varMint)
    sl9.place(relx = 0.22, rely = 0.72, relwidth = 0.05, relheight = 0.04)

    sl10 = Entry(frame_1, font =font_3, textvariable =varRoy)
    sl10.place(relx = 0.22, rely = 0.80, relwidth = 0.05, relheight = 0.04)

    
def Up_sl ():
    pass
def Dw_sl():
    sl1ar = Button(frame_1, font = ('arial', 13), text = '⬇')
    sl1ar.place(relx = 0.61, rely = 0.105, relwidth = 0.025, relheight = 0.025)

Dw_sl()
Up_sl()
SL()
Giá_thành()
frame_1_title()
item() 
root.mainloop()
