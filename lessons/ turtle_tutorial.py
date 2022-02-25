from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
colormode(255)

leo.penup()
leo.goto(20, -60)
leo.pendown()

i: int = 0

leo.fillcolor("pink")
leo.begin_fill()

while (i < 3):
    
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()    

done()