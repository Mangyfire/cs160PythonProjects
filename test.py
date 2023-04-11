from turtle import *
from time import sleep

#background
my_window = Screen() 
my_window.bgcolor("orange")


#house code
penup()
setpos(-50,-50)
pendown()
color("black")
forward (100)
left(90)
forward (100)
left(90)
forward (100)
left(90)
forward (100)
setpos(-50, 50)
right(225)
forward(73)
right(90)
forward(73)


#ground
penup()
setpos(-335,-50)
pendown()
right(315)
forward(800)

#door
penup()
setpos(-20,-50)
pendown()
right(-90)
forward(47)
right(90)
forward(20)
right(90)
forward(47)

#STAMP CIRCLE
#shape("circle")
#stamp()

#circle com
#circle(5,360)


 
#wait for 10
sleep(12)