import turtle

canvas = turtle.Screen()

t = turtle.Turtle()

t.shape("turtle")

import random

import math

innen = math.sqrt(20**2*2)
width = 160

t.speed(0)

def stern(größe):
    t.forward(größe)
    t.left(144)
    t.forward(größe)
    t.left(144)
    t.forward(größe)
    t.left(144)
    t.forward(größe)
    t.left(144)
    t.forward(größe)
    t.left(144)

def sternkreis(größe):
    stern(größe)
    t.right(72)
    t.circle(größe/1.9)
    

t.left(-18)
for i in range(0,15,8):
    t.pu()
    t.goto(random.randint(-150,100),random.randint(-100,100))
    t.pd()
    stern(15+(i/10))
    t.right(72)
    t.circle(8 +(i/20))
t.ht()

t.goto(0,0)
sternkreis(150)

canvas.exitonclick()