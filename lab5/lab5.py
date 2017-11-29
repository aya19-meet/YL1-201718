from turtle import *

import random
colormode(225)

#### Excercise 1

class Square(Turtle):
    def __init__(self,size,color):
        Turtle.__init__(self)
        self.shapesize(size)
        self.shape('square')
        self.color(color)
    def teleport(self):
        self.goto(random.randint(0,100),random.randint(0,100))

square1=Square(5,'blue')
square1.teleport()
##### Excercise 2

        
class Hexagon(Turtle):
    def __init__(self,size):
        Turtle.__init__(self)
        self.begin_poly()
        for i in range(6):
            self.penup()
            self.forward(5)
            self.right(60)
        self.end_poly()
        self.shapesize(size)
        register_shape('hexagon',self.get_poly())
        self.shape('hexagon')

    
##### Excercise 3






