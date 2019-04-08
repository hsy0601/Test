from turtle import *
def draw(radius,color1,color2):
    width(3)
    color("black",color1)
    begin_fill()
    circle(radius/2,180)
    circle(radius,180)
    left(180)
    circle(-radius/2,180)
    end_fill() 
    left(90)
    penup()
    forward(radius*0.35)
    right(90)
    pendown()
    color(color1,color2)
    begin_fill()
    circle(radius*0.15)
    end_fill()
    left(90)
    penup()
    backward(radius*0.35)
    pendown()
    left(90)

def main():
    setup(500,500)
    draw(200,"black","white")
    draw(200,"white","black")
    hideturtle()

main()
mainloop()

    
