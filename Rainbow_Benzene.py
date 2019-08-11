
# Python program to draw
# Rainbow Benzene
# using Turtle Programming
import turtle
wn = turtle.Screen()
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()

t.speed(10)
turtle.bgcolor('black')
for x in range(50):
    t.pencolor()
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)


wn.mainloop()
