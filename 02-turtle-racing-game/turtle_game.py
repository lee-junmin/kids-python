import time
import turtle
import random


player1 = input("Player 1 Name:")
print(player1 +", you are BLUE")

player2 = input("Player 2 Name:")
print(player2 +", you are PINK")

print("ready\nset")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print("GO")



line = turtle.Turtle()
line.color("light green")
line.hideturtle()
line.penup()
line.setpos(-200,-200)
line.pendown()
line.setpos(200,-200)
line.penup()
line.setpos(-200,200)
line.pendown()
line.setpos(200,200)
line.hideturtle()


bob = turtle.Turtle()
bob.shape("turtle")
bob.color("blue")
bob.penup()
bob.setheading(90)
bob.setpos(-100,-200)
bob.pendown()

boblina = turtle.Turtle()
boblina.shape("turtle")
boblina.color("pink")
boblina.penup()
boblina.setheading(90)
boblina.setpos(100,-200)
boblina.pendown()




while bob.ycor() < 200 and boblina.ycor() < 200:
    bob.forward(random.randrange(0,30))
    boblina.forward(random.randrange(0,30))
    time.sleep(0.5)






