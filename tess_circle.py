import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")
tess.speed(4)

tess.penup()
size = 20
# tess.forward(-300)
# for i in range(10):
#     tess.stamp()
#     tess.forward(size)
#
# for _ in range(30):
#     tess.stamp()
#     size = size+3
#     tess.forward(size)
#     tess.right(24)

for _ in range(1):
    tess.stamp()
    tess.forward(size)
for _ in range(20):
    tess.stamp()
    tess.left(-90)
    tess.forward(-50)
for _ in range(20):
    tess.stamp()
    tess.left(-90)
    tess.forward(50)
wn.mainloop()
