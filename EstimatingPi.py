from tkinter import *
from PIL import Image, ImageTk, ImageDraw

root = Tk()
root.title('Estimate Pi')
root.geometry("600x600")

canvas = Canvas(root, width = 600, height = 600, bg = 'white')
canvas.pack()

images = []

def dots(x, y, canvas, color):
    r = 1
    x1 = x - r
    y1 = y - r
    x2 = x + r
    y2 = y + r
    canvas.create_oval(x1, y1, x2, y2, fill = color, outline = '')

canvas.create_rectangle(100, 500, 500, 100, outline='black', width = 3)
canvas.create_oval(100, 500, 500, 100, outline='black', width = 3)

import random
c=[]
a=[]

def right():
    for i in range(1000):
        x = (random.random() * 4) - 2
        y = (random.random() * 4) - 2
        check = False
        for i in range(len(c)):
            if c[i][0] == x and c[i][1] == y:
                check = True
        if check:
            pass
        else:
            c.append([x, y])
            if x*x + y*y <= 4:
                a.append([x, y])
                dots(round(((x+2)*100)+100), round(((y+2)*100)+100), canvas, "pink")
            else:
                dots(round(((x+2)*100)+100), round(((y+2)*100)+100), canvas, "blue")
        pi = 4 * len(a) / len(c)
        print('Pi = ' + str(pi))
    canvas.after(50, right)

right()
root.mainloop()