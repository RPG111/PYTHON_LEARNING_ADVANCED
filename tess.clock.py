import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")

tess.penup()
alex = turtle.Turtle()
alex.color("blue")
alex.shape("arrow")

for _ in range(12):

    tess.left(30)
    tess.forward(120)
    tess.stamp()
    tess.forward(-120)

alex.penup()
for _ in range(12):
    alex.left(30)
    alex.forward(80)
    alex.stamp()
    alex.forward(-80)




wn.mainloop()
