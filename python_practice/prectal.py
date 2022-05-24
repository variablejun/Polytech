from itertools import count
from telnetlib import WONT
from tkinter import *



def drawCircle(x, y, r):
    global count
    print('x : ', x,'y : ', y,'r : ', r)
    count += 1
    canvas.create_oval(x - r, y - r, x + r, y + r)
    canvas.create_text(x, y - r, text=str(count), font=('', 30))
    if r >= radius/2:
        drawCircle(x - r//2, y, r//2)
        drawCircle(x + r//2, y, r//2)
        

count = 0
wSize = 1000
radius = 400

window = Tk()       
canvas = Canvas(window, height=wSize, width=wSize, bg='white')
drawCircle(wSize//2, wSize//2, radius)
canvas.pack()
window.mainloop()