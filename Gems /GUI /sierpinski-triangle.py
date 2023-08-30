from tkinter import *

class SierpinskiTriangle(object):

    def __init__(self, width= 500, height = 500):
        self.level = 3
        self.width, self.height = width, height

    def run(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()
#       self.root.bind("<key>", lambda event: self.onKeyPressed(event))
        #self.canvas.bind("<key>", self.onKeyPressed)
        self.canvas.bind("<Key>", self.onKeyPressed)
        self.redrawAll()
        self.root.mainloop()
    def onKeyPressed(self, event):
        if event.keysym in ["Up", "Right"]:
            self.level += 1
        elif event.keysym in ["Down", "Left"]:
            self.level -= 1
        if self.level < 0: self.level = 0
        self.redrawAll()

    def drawSierpinskiTriangle(self, x, y, size, level):
        # x, y are lower left corner of triangle,
        # size is length of an edge
        x, y = float(x), float(y)
        if level == 0:
            self.canvas.create_polygon(x, y, x + size, y, x + size/2, y - size*(3**.5)/2)
        else:
            self.drawSierpinskiTriangle(x, y, size/2, level-1)
            self.drawSierpinskiTriangle(x+size/2, y, size/2, level-1)
            self.drawSierpinskiTriangle(x+size/4, y- size*(3**.5)/4, size/2, level-1)


    def redrawAll(self):
        self.canvas.delete(ALL)
        self.drawSierpinskiTriangle(self.width/5, self.height/2 + 100, 300, self.level)
        self.canvas.create_text(self.width/2, self.height - 50, 
            text="Level #%d"%self.level, font="Arial 30 bold")
        self.canvas.create_text(self.width/2, self.height - 20, 
            text="Use arrow keys to change level", font="Arial 15")    
anim = SierpinskiTriangle()
anim.run()            
