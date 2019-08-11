import turtle

def draw_multicolor_square(t, sz):
    for i in ["red", "purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("MULTICOLOR SQUARE")

tess = turtle.Turtle()
tess.pensize(3)

size = 20
for i in range(200):
    draw_multicolor_square(tess, size)
    size+=10
    tess.forward(10)
    tess.left(18)

wn.mainloop()