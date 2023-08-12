from turtle import Turtle , Screen
import time
import random

screen = Screen()
screen.setup(700, 700)
screen.bgcolor('black')
screen.tracer(0)
screen.title('Snake')

pos = [(0,0),(0,-20),(0,-40)]

class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segme = []
        self.create_snake()
        self.head = self.segme[0]
    

    def create_snake(self):
        for i in pos:
            self.add_seg(i)
            

    def add_seg(self,pos):
        snake = Turtle('square')
        snake.color('white')
        snake.penup()
        snake.goto(pos)
        self.segme.append(snake)
    
    def grow(self):
        self.add_seg(self.segme[-1].pos())
        


    def move(self):

        for seg in range(len(self.segme) -1,0, -1):
            x= self.segme[seg-1].xcor()
            y = self.segme[seg-1].ycor()
            self.segme[seg].goto(x,y)
            

        self.segme[0].forward(20)

    def f(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def l(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def d(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def r(self):
       if self.head.heading() != 180:
            self.head.setheading(0)

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('red')
        self.shape('circle')
        self.shapesize(0.5, 0.5)
        self.speed('fastest')
        randx = random.randint(-280, 280)
        randy = random.randint(-280, 280)
        self.goto(randx,randy)

    def new(self):
        randx = random.randint(-280, 280)
        randy = random.randint(-280, 280)
        self.goto(randx,randy)

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scorecount = 0
        
        self.penup()
        self.goto(0, 300)
        self.pendown()

    def scores(self):
        self.clear()
        self.hideturtle()
        self.pencolor('white')
        self.write(f'score = {self.scorecount}' , align = 'center', font = ('Arial', 20))
        


snake = Snake()
food = Food()
score = Score()
box = Turtle()

box.penup()
box.goto(-290, 290)
box.pensize(5)
box.pendown()
box.pencolor('white')
for i in range(4):
    box.fd(580)
    box.rt(90)
box.hideturtle()





screen.listen()
screen.onkey(snake.f, 'Up')
screen.onkey(snake.r, 'Right')
screen.onkey(snake.d , 'Down')
screen.onkey(snake.l , 'Left')


game = True
while game ==True:
    
    score.scores()
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.head.xcor() >290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        box.penup()
        box.goto(0,0)
        box.pendown()
        box.write('GAME OVER', align = 'center', font = ('Arial', 20))  
        game  = False      
        
    
    if snake.head.distance(food) < 15:
        food.new()
        score.scorecount +=1
        snake.grow()

    for part in snake.segme:
        if part == snake.segme[0]:
            continue
        elif snake.head.pos() == part.pos():
            box.penup()
            box.goto(0,0)
            box.pendown()
            box.write('GAME OVER', align = 'center', font = ('Arial', 20))  
            game  = False      







screen.exitonclick()