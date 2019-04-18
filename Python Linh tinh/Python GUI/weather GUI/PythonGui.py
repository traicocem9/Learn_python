import tkinter as tk 
from os import path
import requests

width = 600
height = 500

root = tk.Tk()

canvas = tk.Canvas(root, height = height, width = width)
canvas.pack()

# 103defc27b6d172c96c22ba5342bf3fc
# api.openweathermap.org/data/2.5/weather?q=London

def request(weathers):
    try:
        name = weathers['name']
        weather = weathers['weather'][0]['description']
        temp = weathers['main']['temp']
        print_str = 'Thành phố: %s \nThời tiết: %s \nNhiệt độ: %s (F)' % (name, weather, temp)
    except:
        print_str = "Có lỗi khi lấy thông tin do sai tên hoặc mã vùng"
    return print_str
    
def weather(city):
    weather_key = '103defc27b6d172c96c22ba5342bf3fc'
    url = 'https://api.openweathermap.org/data/2.5/weather?'
    params = {'APPID':weather_key,'q':city, 'units':'imperial'}
    response = requests.get(url, params = params)
    weathers = response.json()
    label['text'] = request(weathers)


img_file = path.join(path.dirname(__file__), 'img')
img_path = path.join(img_file, "landscape.png")

bg_image = tk.PhotoImage(file=img_path)
bg_label = tk.Label(root, image = bg_image)
bg_label.place(relheight = 1, relwidth = 1)

frame = tk.Frame(root, bg = '#99ccff')
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n')

frame_2 = tk.Frame(root, bg= "#99ccff")
frame_2.place(relx = 0.5, rely = 0.9, relwidth = 0.75, relheight = 0.6, anchor = 's')

button = tk.Button(frame, text = "Lấy thông tin", activeforeground = "red",command = lambda: weather(entry.get()),font = ('Couier',18))
button.place( relx = 0.59, rely = 0.5, relwidth = 0.4, relheight = 0.9, anchor = 'w')   

label = tk.Label(frame_2,text = " ",anchor = 'nw', font = ('Couier',18), justify = 'left', bd = 4)
label.place(relx = 0.025 , rely = 0.02, relwidth = 0.95, relheight = 0.95 )

entry = tk.Entry(frame)
entry.place(relx = 0.3, rely = 0.95, relwidth = 0.55, relheight = 0.9, anchor = 's')

root.mainloop()