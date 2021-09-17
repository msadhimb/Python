import turtle

turtle.bgcolor("black")
bob = turtle.Turtle()  

def curves():
    for i in range(200):
        bob.right(1)
        bob.forward(1)

bob.speed(0)
bob.color("yellow", "purple")
bob.begin_fill()

bob.left(140)
bob.forward(125)
curves()

bob.left(120)
curves()
bob.forward(125)

bob.end_fill()
bob.hideturtle()