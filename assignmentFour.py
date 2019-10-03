from turtle import *
import random

window = Screen()
window.bgcolor("#FBEEE6")
colors=['orange', '#8B008B', '#FF0011', '#DC143C']

speed(0)

for n in range(4):
    def square ():
      pencolor(colors[2])
      forward(80)
      left(90)
      pencolor(colors[3])
      forward(80)
      left(90)
      pencolor(colors[3])
      forward(80)
      left(90)
      pencolor(colors[2])
      forward(80)

    penup()
    goto(random.randint(-160, 160), random.randint(-160, 160))
    pendown()
    pensize(random.randint(1, 2))

    for i in range(32):
        square()
        left(80)

for n in range(4):
    def smallSquare ():
      pencolor(colors[0])
      forward(50)
      left(90)
      pencolor(colors[3])
      forward(50)
      left(90)
      pencolor(colors[3])
      forward(50)
      left(90)
      pencolor(colors[0])
      forward(50)

    penup()
    goto(random.randint(-400, 400), random.randint(-400, 400))
    pendown()
    pensize(1)

    for i in range(32):
        smallSquare()
        left(80)

hideturtle()
        