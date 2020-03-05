# Sierpinski Triangle

from tkinter import *
import random
class makeTriangles():

    def __init__(self):

        self.wn = Tk()
        self.wn.geometry("1350x750")
        self.wn.title("Sierpinski Triangle")
        self.canvas = Canvas(self.wn, height = 750, width = 1350, bg = "white")
        self.canvas.pack()
        self.canvas.bind('<Button-1>', self.obtainPoint)
        
        self.count = 0
        self.letters = ["point A","point B","point C", "the starting point"]
        self.points = []
        self.instruct()
        
        
        self.iterations = Label(self.canvas, text = "Iterations: 0", bg = "white", font = "Arial 20")
        self.iterations.place(x = 100, y = 30)
        self.slider = Scale(self.canvas, label = "                     Iterations", from_ = 100, to = 100000, troughcolor = "black", orient = HORIZONTAL, length = 250, bg = "white")
        self.slider.place(x = 1000, y = 30)
        self.radSlider = Scale(self.canvas, label = "                       Radius", from_ = 0.05, to = 10, troughcolor = "black", command = self.setRadius, resolution = 0.05, orient = HORIZONTAL, length = 250, bg = "white")
        self.radSlider.place(x = 1000, y = 100)
        self.radius = self.radSlider.get()
        self.button = Button(self.canvas, text = "Start", command = self.startPlacing, width = 15, bg = "black", fg = "white", state = DISABLED)
        self.button.place(x = 100, y = 110)
        self.wn.mainloop()
        
    def obtainPoint(self, event):
        
        self.restart = False
        
        if self.count == 3:
            self.startPoint = [event.x, event.y]
            self.canvas.create_oval(self.startPoint[0]-2, self.startPoint[1]-2, self.startPoint[0]+2, self.startPoint[1]+2, fill = "red", outline = "", tags = "points")

        else:
            self.points.append([event.x, event.y])
            self.canvas.create_oval(self.points[self.count][0]-self.radius, self.points[self.count][1]-self.radius, self.points[self.count][0]+self.radius, self.points[self.count][1]+self.radius, fill = "black", outline = "", tags = "startpoints")            

        self.count += 1
        self.instruct()
        
    def instruct(self):
        
        
        if self.count == 4:
            self.canvas.bind('<Button-1>', self.doNothing)
            self.button["state"] = NORMAL
            
            self.canvas.create_rectangle(520, 50, 820, 70, tags = "bar")
            
            self.start = Label(self.canvas, text = "Starting point: " + str(format(self.startPoint[0], ".2f")) + ", " + str(format(self.startPoint[1], ".2f")), bg = "white", font = "Arial 15")
            self.start.place(x = 100, y = 70)
            return
        self.point = Label(self.canvas, text = "Place " + self.letters[self.count], bg = "white", font = "Arial 15", width = 30, anchor = W)
        self.point.place(x = 100, y = 70)
            

        
    def setRadius(self, value):

        self.radius = eval(value)
        
                
    def startPlacing(self):
        self.radSlider["state"] = DISABLED
        self.slider["state"] = DISABLED
        self.canvas.delete("points")
        self.count = 0
        self.button["text"] = "Stop"
        self.button["command"] = self.stop
        self.canvas.create_oval(self.startPoint[0]-2, self.startPoint[1]-2, self.startPoint[0]+2, self.startPoint[1]+2, fill = "red", outline = "", tags = "points")
        self.lastPoint = self.startPoint
        
        for i in range(self.slider.get()):
            if not self.restart:
                point = random.randint(0,2)
                
                self.lastPoint = [(self.lastPoint[0]+self.points[point][0])/2,(self.lastPoint[1]+self.points[point][1])/2]
                self.canvas.create_oval(self.lastPoint[0]-self.radius, self.lastPoint[1]-self.radius, self.lastPoint[0]+self.radius, self.lastPoint[1]+self.radius, fill = "black", outline = "", tags = "points")
                self.iterations["text"] = "Iterations: " + str(i+1)
                self.canvas.delete("progress")
                self.canvas.create_rectangle(520, 50, 520+((i+1)/self.slider.get())*300, 70, fill = "green", tags = "progress")
                self.canvas.update()
            else:
                return

        self.button["text"] = "Start"
        self.button["command"] = self.startPlacing
        self.radSlider["state"] = NORMAL
        self.slider["state"] = NORMAL
            

    def doNothing(self, event):
        return

    def stop(self):
        self.restart = True
        self.button["text"] = "Start"
        self.button["command"] = self.startPlacing
        self.canvas.bind('<Button-1>', self.obtainPoint)
        self.button["state"] = DISABLED
        self.slider["state"] = NORMAL
        self.radSlider["state"] = NORMAL
        self.canvas.delete("bar","progress", "points", "startpoints")
        self.iterations["text"] = "Iterations:"
        self.points = []
        self.instruct()
        
        
        

            

            
                



makeTriangles()
