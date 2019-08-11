import turtle

def draw_square(t, colr, sz):
    size = 10
    alex.pendown()
    alex.color(colr)
    alex.pensize(sz)
    alex.right(90)
    alex.forward(size)
    i = 10
    for _ in range(60):

        alex.right(89)
        alex.forward(size + i)
        alex.right(89)
        alex.forward(size + i)
        i += 10


wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("4 SQUARES")

alex = turtle.Turtle()

draw_square(alex, "hotpink", 5)

wn.mainloop()
