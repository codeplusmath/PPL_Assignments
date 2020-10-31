import turtle
import math

t= turtle.Turtle()

s=turtle.Screen()
s.bgcolor("white")
t.pencolor("orange")

t.pensize(5)
t.penup()
t.goto(-100,100)
t.pendown()


class shape:
    def __init__(self, sides = 0, length = 0) :
        self.sides = sides
        self.length = length

class curve(shape):
    def info(self):
        print("A curve is a continuous and smooth flowing line without any sharp turns.")

class dot(shape):
    def info(self):
        print("A small, round mark")
    def show(self):
        t.fd(1)



class polygon(shape):
    def info(self):
        print("In geometry, a polygon can be defined as a flat or plane, two-dimensional  with straight sides.")


class line(shape):
    def show(self):
        t.fd(self.length)
        
        
class triangle(polygon):
    def show(self):
        for i in range(3):
           t.forward(self.length) 
           t.right(120)
        
        
class square(polygon):
    def show(self):
        for i in range(4):
           t.forward(self.length) 
           t.right(90)
    

class pentagon(polygon):
    def show(self):
        for i in range(5):
           t.forward(self.length) 
           t.right(72) 


class hexagon(polygon):
    def show(self):
        for i in range(6):
           t.forward(self.length) 
           t.right(60)


class octagon(polygon):
    def show(self):
        for i in range(8):
           t.forward(self.length) 
           t.right(45)


class circle(curve):
    def show(self):
        t.circle(self.length)
        
class sin(curve):
    def show(self):
        for angle in range(-180, 180):
            t.goto(angle, math.sin(math.radians(angle))*100)


c1 = circle(0,100)
c1.show()
hex1 = hexagon(6, 100)
hex1.show()
ot = octagon(8, 100)
ot.show()
si = sin()
si.show()
turtle.exitonclick()



  
