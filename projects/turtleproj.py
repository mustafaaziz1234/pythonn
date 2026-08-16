import turtle
screen = turtle.Screen()
screen.bgcolor("black")
pointer = turtle.Turtle()
title = screen.title("project")
speed = turtle.speed("fastest")
pensize = pointer.pensize(2)
colors = [ "red","cyan","blue","orange", "yellow","lime", "magenta" ]

def draw_petal(size,color):
    pointer.color(color)
    pointer.begin_fill()

    for _ in range(2):
       pointer.circle(size , 60)
       pointer.left(120)

    pointer.end_fill()

#doesnt matters if we put the colors list here or at the beginning.

for i in range(36):
    draw_petal(60, colors[i % len(colors)])
    pointer.right(10)

pointer.penup()
pointer.goto(0,-25)
pointer.pendown()
pointer.begin_fill
pointer.circle(25)
pointer.color("white")
pointer.end_fill()

turtle.done()