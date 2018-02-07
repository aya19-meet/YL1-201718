from turtle import*
import random
import time
import turtle
import math 
class Ball(Turtle):
    def __init__(self,x,y,dx,dy,r,color):
        Turtle.__init__(self)
        self.penup()
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.r = r
        self.color(color)
        self.goto(x,y)
        self.shape('circle')
        self.size=(r/10)
    def move(self,width,height):
        self.width=width
        self.height=height
        current_x=self.x
        new_x=self.dx+current_x
        current_y=self.y
        new_y=self.dy+current_y
        right_ball=new_x+self.r
        left_ball=new_x-self.r
        up_ball=new_y+self.r
        down_ball=new_y-self.r
        self.goto(new_x,new_y)
        if (right_ball>width/2):
            self.dx = self.dx*-1
        if (left_ball>width/-2):
            self.dx=self.dx*-1
        if (up_ball>height/2):
            self.dy=self.dy*-1
        if (down_ball>height/-2):
            self.dy=self.dy*-1


##football=Ball(0,0,30,30,5,'red')
##football.move(100,100)

# Agario.py logic


turtle.tracer(delay=0)
turtle.hideturtle()

RUNNING=True
SLEEP=0.0077
SCREEN_WIDTH=round(turtle.getcanvas().winfo_width()/2)
SCREEN_HEIGHT=round(turtle.getcanvas().winfo_height()/2)


#### PART 0 ######

MY_BALL=Ball(0,0,30,30,5,'red')

NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=100
MINIMUM_BALL_DX=-5
MAXIMUM_BALL_DX=5
MINIMUM_BALL_DY=-5
MAXIMUM_BALL_DY=5
BALLS=[]

for i in range(NUMBER_OF_BALLS):
    x = random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
    y = random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS)
    dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
    dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
    r = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
    color = (random.random(),random.random(),random.random())

    ball=Ball(x,y,dx,dy,r,color)
    BALLS.append(ball)


########### PART 1 ########

def move_all_balls():
    for b in BALLS:
        b.move(SCREEN_WIDTH,SCREEN_HEIGHT)

###### PART 2 #########

def collide(ball_a,ball_b):
    if ball_a==ball_b:
        return False
    xa=ball_a.xcor()
    ya=ball_a.ycor()

    xb=ball_b.xcor()
    yb=ball_b.ycor()

    D = math.sqrt(math.pow((xa-xb),2)+math.pow((ya-yb),2))

    if D+10<=ball_a.r+ball_b.r:       
        return True
    else:
        return False

##### PART 3 #######

def check_all_balls_collision():
    for ball_a in BALLS:
        for ball_b in BALLS:
            if collide(ball_a,ball_b)==True:
                radius_a=ball_a.r
                radius_b=ball_b.r
                print(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
                x = random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
                y = random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS)
                dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
                r = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
                color = (random.random(),random.random(),random.random())
                if radius_a > radius_b:
                    ball_b.goto(x,y)
                    ball_a.r+=1
                    ball_b.r=r
                    ball_b.x=x
                    ball_b.y=y
                    ball_b.dx=dx
                    ball_b.dy=dy
                    ball_b.color(color)
                    ball_a.shapesize(r/10)
                    ball_b.shapesize(r/10)
                else:
                    ball_a.goto(x,y)
                    ball_b.r+=1
                    ball_a.r=r
                    ball_a.x=x
                    ball_a.y=y
                    ball_a.dx=dx
                    ball_a.dy=dy
                    ball_a.color(color)
                    ball_a.shapesize(r/10)
                    ball_b.shapesize(r/10)

#### PART 4 ####

def check_myball_collision():
    for ball in BALLS:
        if collide(MY_BALL,ball)==True:
                my_r=MY_BALL.r
                ballr=ball.r
                x = random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
                y = random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS)
                dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
                r = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
                color = (random.random(),random.random(),random.random())

                if ballr>my_r:
                  return False
                elif ballr<my_r:
                  MY_BALL.r+=1
                  MY_BALL.shapesize(r/10)
                  ball.r=r
                  ball.x=x
                  ball.y=y
                  ball.dx=dx
                  ball.dy=dy
                  ball.color(color)

                
                return True


####### PART 5 ######

def movearound(event):
    X=event.x-SCREEN_WIDTH
    Y=SCREEN_HEIGHT-event.y
    MY_BALL.goto(X,Y)
###### PART 5.1 #######

turtle.getcanvas().bind("<Motion>",movearound)
turtle.getscreen().listen()

####### PART 6 #######

while RUNNING==True:
    if SCREEN_WIDTH != turtle.getcanvas().winfo_width()/2 or SCREEN_HEIGHT != turtle.getcanvas().winfo_height()/2:     
            SCREEN_WIDTH=round(turtle.getcanvas().winfo_width()/2)
            SCREEN_HEIGHT=round(turtle.getcanvas().winfo_width()/2)
    move_all_balls()
    check_all_balls_collision()
    MY_BALL.move(SCREEN_WIDTH,SCREEN_HEIGHT)
    RUNNING=check_myball_collision
    turtle.update()
    time.sleep(SLEEP)
    

    

                  
    
                  
