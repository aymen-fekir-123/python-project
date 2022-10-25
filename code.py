from tkinter import*
from math import cos, sin
dx, ang, sz, y, x = 1, 0.1, 20, 0, 0
class Aymen_class_root():
    def __init__(self):
        self.coords=[]
        self.stack=[]
        for i in range(3):
            self.coords.append([120,120])
        for x,y in self.coords:
            root=canva.create_oval(x,y,x+sz,y+sz,fill="red",tag="aymen")
            self.stack.append(root)
def move_cirlclian(coorp):
    global ang,x1,y1,x,y
    x1,y1=x,y
    ang = ang +0.1
    x, y = cos(3*ang), sin(2*ang)
    x, y = 120 * x + 150,  120 * y + 150
    coorp.coords.insert(0,[x,y])
    disk=canva.create_oval(x,y,x+sz,y+sz,fill="red",tag="aymen")
    coorp.stack.insert(0,disk)
    del (coorp.coords[-1])
    canva.delete(coorp.stack[-1])
    del(coorp.stack[-1])
    window.after(35, move_cirlclian, coorp)
window=Tk()
canva=Canvas(window,bg="white",width=500,height=500)
canva.pack()
coorp=Aymen_class_root()
move_cirlclian(coorp)
window.mainloop()
