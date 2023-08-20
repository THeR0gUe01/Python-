from turtle import Turtle, Screen 
import time
screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

line = Turtle()
line.penup()
line.pencolor('white')
line.width(1)
line.goto(0,400)
line.pendown()
line.goto(0,-400)

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score1 = 0 
        self.score2 =0
        self.up()
        
    def up(self):
        self.goto(100,200)
        self.write(self.score1, align = 'center', font = ('Courier', 80 , 'normal'))
        self.goto(-100,200)
        self.write(self.score2, align = 'center', font = ('Courier', 80 , 'normal'))
        
    def scored1(self):
        self.clear()
        self.score1 +=1
        self.up()
    def scored2(self):
        self.clear()
        self.score2 +=1
        self.up()

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.shapesize(0.5,0.5)
        self.penup()
        self.goto(0,0) 
        self.ymove = 10
        self.xmove = 10
        
        self.count = 0.1
    def move(self): 
        x = self.xcor()
        y = self.ycor()
        
        newy = y + self.ymove
        newx = x +self.xmove
        self.goto(newx,newy)
        
    def bounce(self):
        self.ymove *= -1
    def hitbounce(self):
        self.xmove *= -1
        self.count *= 0.9
    def reset(self):
        self.goto(0,0)
        self.count = 0.1
        self.hitbounce()
        
        
class Paddle(Turtle):
    def __init__(self) :
        super().__init__()
    def make_paddle(self , pos):
        self.goto(pos)
        self.shape('square' )
        self.color('white')
        self.lt(90)
        self.shapesize(1,7)
        self.penup()
        
    def f(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def d(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
    
pad1 = Paddle()
pad1.make_paddle((350,0))
pad2 = Paddle()
pad2.make_paddle((-350,0))

ball = Ball()
score = Score()



screen.listen()
screen.onkey(pad1.f, 'Up')
screen.onkey(pad1.d , 'Down')

screen.onkey(pad2.f, 'w')
screen.onkey(pad2.d , 's')

game = True
while game ==True:
    time.sleep(ball.count)
    screen.update()
    ball.move()
    
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()
        
    if ball.distance(pad1)<60 and ball.xcor() >340:
        ball.hitbounce()
        
    if ball.distance(pad2)< 60 and ball.xcor() < -340:
        ball.hitbounce()
    
    elif ball.xcor() > 380:
        score.scored1()
        ball.reset()
    elif ball.xcor() < -380:
        score.scored2()
        ball.reset()
        
    
screen.exitonclick()