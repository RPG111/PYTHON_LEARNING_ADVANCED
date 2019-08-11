import turtle

def draw_square(t, colr, sz):
    for _ in range(4):
        for _ in range(4):
            alex.color(colr)
            alex.pensize(sz)
            alex.pendown()
            alex.forward(20)
            alex.left(90)
        alex.penup()
        alex.forward(30)


wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("4 SQUARES")

alex = turtle.Turtle()

draw_square(alex, "hotpink", 5)

wn.mainloop()
