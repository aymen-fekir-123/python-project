from tkinter import*
sz,dx,dy=50,1,0
class Snake_man():
    def __init__(self):
        self.coordsnake = []
        self.snakef = []
        for i in range(39):
            self.coordsnake.append([0, 0])
        for x, y in self.coordsnake:
            squar = canvas.create_rectangle(x, y, x + sz, y + sz, fill="red", tag="scoorp")
            self.snakef.append(squar)
class Food_object():
    def __init__(self):
        self.food1 = []
        self.ovale = []
        x , y, ds, du = 50, 0, 1, 0
        for i in range(0, 34):
            if i >= 8 and i <= 16:
                ds, du = 0, 1
            elif i >= 16 and i <= 25:
                ds, du = -1, 0
            elif i >= 25 and i <= 34:
                ds, du = 0, -1
            self.food1.append([x, y])
            x, y = x + sz * ds, y + sz * du
        for x1, y1 in self.food1:
            ovale1 = canvas.create_rectangle(x1, y1, x1+sz, y1+sz, fill="white", tag="Foof")
            self.ovale.append(ovale1)
def accélerer(scoorp, object):
    global dx, dy
    x, y = scoorp.coordsnake[0]
    n = len(object.food1)
    if x > 450:
        x, dx, dy = 450, 0, 1
    elif y > 450:
        y, dx, dy = 450, -1, 0
    elif x < 0:
        x, dx, dy = 0, 0, -1
    elif y < 0:
        y, dx, dy = 0, 1, 0
    x, y = x + dx * sz, y + dy * sz
    if n != 1:
        for i in range(n - 1):
            x1, y1 = object.food1[i]
            if x1 == x and y1 == y:
                scoorp.coordsnake.insert(0, [x, y])
                squaar = canvas.create_rectangle(x, y, x + sz, y + sz, fill="red", tag="scoorp")
                scoorp.snakef.insert(0, squaar)
                del (object.food1[i])
                canvas.delete(object.ovale[i])
                del (object.ovale[i])
    scoorp.coordsnake.insert(0, [x, y])
    squaar = canvas.create_rectangle(x, y, x + sz, y + sz, fill="red", tag="scoorp")
    scoorp.snakef.insert(0, squaar)
    del (scoorp.coordsnake[-1])
    canvas.delete(scoorp.snakef[-1])
    del (scoorp.snakef[-1])
    canvas.delete(object.ovale[-1])
    fenettre.after(50, accélerer, scoorp, object)
fenettre=Tk()
canvas = Canvas(fenettre, bg="white", width=500, height=500)
canvas.pack()
scoorp = Snake_man()
object = Food_object()
accélerer(scoorp, object)
fenettre.mainloop()