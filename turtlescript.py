import turtle

alex = turtle.Turtle()
alex.shape("turtle")
alex.screen.bgcolor("black")
alex.color("red")
# alex.hideturtle()
# alex.width(5)

def hexagon(size):
    for i in range(6):
        alex.forward(size)
        alex.right(60)

def hexagons(size):
    for i in range(6):
        for i in range(6):
            alex.forward(size)
            alex.left(60)
        alex.forward(size)
        alex.right(60)

def simplestar(size):
    for i in range(5):
        alex.forward(size)
        alex.right(144)

def star(size):
    for i in range(5):
        alex.forward(0.38*size)
        alex.penup()
        alex.forward(0.24*size)
        alex.pendown()
        alex.forward(0.38*size)
        alex.right(144)

simplestar(500)

turtle.Screen().mainloop()
