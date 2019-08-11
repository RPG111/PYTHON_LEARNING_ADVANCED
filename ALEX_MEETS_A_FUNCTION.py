import turtle

def draw_square(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("ALEX MEETS A FUNCTION")

alex = turtle.Turtle()
draw_square(alex, 50)

wn.mainloop()