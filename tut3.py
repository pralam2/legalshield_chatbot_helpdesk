import turtle
Turtle = turtle.Turtle(shape= "turtle")
Turtle.speed(5)
Turtle.shape("square")
def cantorStart (a, b, c, d):

    if d<=0:
        return 0
    else:

        Turtle.penup();
            Turtle.setpos(a,c)
        Turtle.pendown();
            Turtle.setpos(b,c)
        Turtle.penup();
        size = a-b;

        cantorStart(a,b+size/3, c-10, d-1)
        cantorStart(a+2*size/3, b, c-10, d-1)

        Turtle.pencolor("Black")
        Turtle.pensize(5)
        cantorStart(-150,150,80,8);
input("enter to quit")
