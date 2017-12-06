from turtle import*
import random
import math 

class Ball(Turtle):
    def __init__(self,radius,color,speed):
        Turtle.__init__(self)
        self.shape("circle")
        self.shapesize(radius/10)
        self.radius = radius
        self.color(color)
        self.speed(speed)


ball1=Ball(10,'red',1)
ball1.goto(30,0)
ball2=Ball(20,'blue',1)

##def check_coll(ball1,ball2):
##      if math.sqrt(math.pow(ball1.xcor()-ball2.xcor(),2)+math.pow(ball1.ycor()-ball2.ycor(),2))<=ball1.radius+ball2.radius:
##          print('collision why did it stop working')
##          ball1.color("green")
##          ball2.color("purple")
##          

check_coll(ball1,ball2)

listofballs=[ball1,ball2]

def checkcheck(listofballs):
    for index1 in range(len(listofballs)):
        for index2 in range(index1,len(listofballs)):
            check_coll(listofballs[index1],listofballs[index2])
    
checkcheck(listofballs)
