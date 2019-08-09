import turtle
import random
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Tess & Alex")

tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(5)

alex = turtle.Turtle()
alex.color("red")
alex.pensize(9)

tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)

tess.right(180)
tess.forward(80)

alex.forward(80)
dist = 20
for _ in range(20):

    alex.color(random.choice(["blue", "red", "black", "white"]))
    alex.forward(dist)
    alex.left(90)
    dist += 10

for _ in [0, 1, 2, 3]:
    alex.forward(50)
    alex.left(90)
dist = 20

for _ in range(20):

    alex.color(random.choice(["blue", "red", "black", "white"]))
    alex.forward(dist)
    alex.left(90)
    dist += 10
dist = 20
for _ in range(20):

    alex.color(random.choice(["blue", "red", "black", "white"]))
    alex.forward(dist)
    alex.left(90)
    dist += 10
dist = 20
for _ in range(20):

    alex.color(random.choice(["blue", "red", "black", "white"]))
    alex.forward(dist)
    alex.left(90)

    dist += 10
dist = 20
for _ in range(20):

    alex.color(random.choice(["blue", "red", "black", "white"]))
    alex.forward(dist)
    alex.left(90)
    dist += 10
dist = 20
wn.mainloop()

