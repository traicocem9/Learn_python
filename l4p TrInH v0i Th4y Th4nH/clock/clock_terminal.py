#https://github.com/paydrone/Python-Terminal-Clock/blob/master/clock.py
	
from time import sleep
import os
import datetime
import ctypes
import platform

opsys = platform.platform()
if opsys  == 'Windows':
     ctypes.windll.kernel32.SetConsoleTitleA("Python Clock")
     #Changes terminal size
     os.system("mode con: cols=90 lines=11")

list = [
"""
 ███████
██     ██
██     ██
██     ██
██     ██
██     ██
 ███████
""",
"""
   ███ 
  ████
██████
   ███
   ███
   ███
█████████
""",
"""
████████
      ██
      ██
████████
██
██
████████
""",
"""
████████
      ██
      ██
████████
      ██
      ██
████████
""",
"""
██    ██
██    ██
██    ██
████████
      ██
      ██
      ██
""",
"""
████████
██
██
████████
      ██
      ██
████████
""",
"""
████████
██
██
████████
██    ██
██    ██
████████
""",
"""
████████
      ██
      ██
    ██
   ██
   ██
   ██
""",
"""
 ███████
██     ██
██     ██
█████████
██     ██
██     ██
 ███████
""",
"""
█████████
██     ██
██     ██
█████████
       ██
       ██
█████████
"""
]
colon = '''


  ██
  ██

  ██
  ██'''


done = True
while(done):

#    if opsys == 'Windows':
#         os.system('cls')
#    else:
#        print ("\n"*15)

    time = str(datetime.datetime.now())[11:19]

    lines = ["","","","","","","","",""]
    line = 0

    numbers = [[],[],[],[],[],[],[],[]]
    for x in range(8):
        if time[x].isdigit():
            #print list[x]
            numbers[x] = list[int(time[x])].splitlines()
        elif time[x] == ":":
            numbers[x] = colon.splitlines()

    for x in range(9):
        X = ""
        for i in range(9):
            #print x,i
            try:
                if i != 8:
                    X += str(numbers[i][line]).ljust(10)
                else:
                    X += str(numbers[i][line])
            except:
                X += "         "
        lines[x] += X
        line += 1
	
    #print lines

    for x in range(9):
        print (lines[x])

    #done = False

    print
    sleep(0.1)
    os.system("clear")




