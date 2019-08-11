import turtle

def draw_square(t, colr, sz):
    size = 20
    for _ in range(4):
        for _ in range(4):
            alex.pendown()
            alex.color(colr)
            alex.pensize(sz)

            alex.forward(size)
            alex.left(90)
        alex.penup()
        size += 20
        alex.right(135)
        alex.forward(pow(200, 1/2))
        alex.left(135)

d
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("4 SQUARES")

alex = turtle.Turtle()

draw_square(alex, "hotpink", 5)

wn.mainloop()
