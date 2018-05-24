import turtle

def draw_CantorSet(mypen,x,y,length):
    x_1 = x
    y_1 = y

    for itr in range(8):

        mypen.color("black")

        mypen.penup()

        mypen.setposition(x,y)

        mypen.pendown()

        mypen.pensize(5)

        mypen.forward(length)

        y=y-10

    x1 = x_1/3

    y1 = y_1

    l1 = length/3

    for itr in range(8):

        mypen.penup()

        mypen.setposition(x1,y1)

        mypen.color("white")

        mypen.pendown()

        mypen.pensize(5)

        mypen.forward(11)

        size=y1-x1;

    draw_CantorSet(x1,x1+size/3,length-1)
    draw_CantorSet(y1,x1+2*size/3,length-1)

if __name__ == "__main__":

    mypen = turtle.Turtle()


    draw_CantorSet(mypen,-150,80,300)

mypen.getscreen()._root.mainloop()
