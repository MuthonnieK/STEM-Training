import sys
import turtle

def border(t, screen_x, screen_y):
"""(turtle, int, int)
draws a canvas around the canvas in red
"""

#lift the pen and move the turtle to the centre
t.penup()
t.home()

#move to the lower corner of the screen; leaves the turtle
#facing west 
t.forward(screen_x / 2)
t.right(90)
t.forward(screen_y / 2)
t.setheading(180) #t.right(90) would also work.

#draw border
t.pencolor('red')
t.pendown()
t.pensize(10)
for distance in (screen_x, screen_y, screen_x, screen_y):
    t.forward(distance)
    t.right(90)
    
 #raise the pen and move the turtle home again; its a good idea to
 #to leave the turtle in a known state
t.penup()
t.home()

def square(t, size, color):
"""(turtle, int, string)
draw a square of the chosen color and size
"""
t.pencolor(color)
t.pendown()
for i in range(4):
    t.forward(size)
    t.right(90)

def main():
    #create screen and tirtle.
    screen= turtle.Screen()
    screen.title('Square Demo')
    screen_x, screen_y= screen.sreensize()
    t= turtle.Tutle()

#uncomment to draw the graphics as quickly as possible.
##t.speed(0)

#draw a border around the canvas
border(t, screen_x, screen_y)

#draw a set of nested squares, varying the colors.
#the colors are 10%, 20%, etc. of half the size of the canvas.
colors= ['red', 'orange', 'yellow', 'green','blue','violet']
t.pensize(3)
for i, color in enumerate(colors):
    square(t, (screen_y/2)/10*(i+1),color)
print('Hit any key to exit')
dummy= input()
if_name_== '_main_':
    main()
