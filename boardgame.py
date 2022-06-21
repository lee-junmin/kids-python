import turtle
import random
import time

turtle.screensize(canvwidth=400, canvheight=300)

square = turtle.Turtle()
square.fillcolor("light blue")
square.pencolor("light blue")
square.speed(500)
square.hideturtle()

for i in range(20):
    square.penup()
    square.setpos(-50, 40 *(i - 10))
    square.begin_fill()
    square.pendown()
    square.forward(100)
    square.left(90)
    square.forward(35)
    square.left(90)
    square.forward(100)
    square.left(90)
    square.forward(35)
    square.left(90)
    square.end_fill()


t1 = turtle.Turtle()
t1.shape("turtle")
t1.setheading(90)
t1.penup()
t1.setpos(-30,-385)

t2 = turtle.Turtle()
t2.shape("turtle")
t2.setheading(90)
t2.penup()
t2.setpos(30,-385)

def move(turt, count):
    for i in range(count):
        turt.forward(40)
        time.sleep(0.2)
        if turt.ycor() >= 375:
            break

def display():
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print("")
    print("you rolled...")
    time.sleep(0.5)
    print("")
    time.sleep(1)

while True:
    input("Player1, press enter to roll the dice")
    roll = random.randrange(1,7)
    display()
    print(roll,"!!!")
    print("")
    time.sleep(1)
    move(t1,roll)

    if t1.ycor() >= 375:
        print("Player1 wins!!!")
        break

    input("Player2, press enter to roll the dice")
    roll = random.randrange(1,7)
    display()
    print(roll,"!!!")
    print("")
    time.sleep(1)
    move(t2,roll)

    if t2.ycor() >= 375:
        print("Player2 wins!!!")
        break







