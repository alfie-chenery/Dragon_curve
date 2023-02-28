cycle = 1
old = "R" #first iteration is a single right turn

iterations = int(input("How many iterations do you want to do? Recommended no more han 20. "))
while cycle<iterations:
    new = old + "R"
    flip = old[::-1]
    swap = ""
    for char in range(0,len(flip)):
        if flip[char] == "R":
            swap = swap + "L"
        elif flip[char] == "L":
            swap = swap + "R"
            
    new = old + "R" + swap
    old = new
    cycle = cycle + 1

size = int(input("Enter size of curve Recommended no more than 10. "))
import turtle
wn = turtle.Screen()
wn.screensize(canvwidth = 10000, canvheight = 10000, bg = "black")
wn.delay(0)
dragon = turtle.Turtle()
dragon.color("white")
dragon.hideturtle()
dragon.speed(0)
dragon.left(90)
dragon.forward(1)


for char in range(0,len(new)): #create a new variable where all turns are the alternative based of of flip variable
    if new[char] == "R":
        dragon.right(90)
        dragon.forward(size)
    elif new[char] == "L":
        dragon.left(90)
        dragon.forward(size)

import time
wn.bgcolor("green")
time.sleep(1)
wn.bgcolor("black")
wn.exitonclick()
