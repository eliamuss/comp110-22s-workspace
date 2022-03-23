"""A beautiful sunset day at the beach with a boat and beach house, but make it Star Wars."""

__author__ = "730411607"

from turtle import Turtle, colormode, done, end_fill, forward, pencolor
import turtle
import random
colormode(255)

colormode
end_fill
forward
pencolor
turtle

my_turtle: Turtle = Turtle()
sun_random = random.randint(35, 100) 


def main() -> None:
    """This is setting up the start pointings for each graphic of my programming scene."""
    sunset_one(my_turtle, -300, 300)
    sunset_two(my_turtle, -300, 200)
    sunset_three(my_turtle, -300, 100)
    sunset_four(my_turtle, -300, 0)
    ocean_one(my_turtle, 150, -100)
    ocean_two(my_turtle, 0, -100)
    beach_one(my_turtle, -300, -100)
    beach_two(my_turtle, -150, -100)
    house_base(my_turtle, -200, -200)
    house_roof(my_turtle, -200, -100)
    boat(my_turtle, 100, -200)
    sun_one(my_turtle, 0, 150, sun_random)
    sun_two(my_turtle, 100, 100, sun_random)
    done()


def sunset_one(my_turtle: Turtle, x: float, y: float) -> None:
    """Makes the first rectangular layer of my sunset: violet."""
    my_turtle.speed(10)
    my_turtle.color(134, 1, 175)
    my_turtle.penup()
    my_turtle.goto(-300, 300)
    my_turtle.pendown()
    my_turtle.fillcolor(134, 1, 175)
    my_turtle.begin_fill()

    i: int = 0
    while i < 2:
        my_turtle.forward(600)
        my_turtle.right(90)
        my_turtle.forward(100)
        my_turtle.right(90)
        i += 1
    
    my_turtle.end_fill()


def sunset_two(my_turtle: Turtle, x: float, y: float) -> None:
    """Makes the second rectangular layer of my sunset: navy."""
    my_turtle.speed(10)
    my_turtle.color(0, 0, 128)
    my_turtle.penup()
    my_turtle.goto(-300, 200)
    my_turtle.pendown()
    my_turtle.fillcolor(0, 0, 128)
    my_turtle.begin_fill()

    i: int = 0
    while i < 2:
        my_turtle.forward(600)
        my_turtle.right(90)
        my_turtle.forward(100)
        my_turtle.right(90)
        i += 1
    
    my_turtle.end_fill()


def sunset_three(my_turtle: Turtle, x: float, y: float) -> None:
    """Makes the third rectangular layer of my sunset: orange."""
    my_turtle.speed(10)
    my_turtle.color(255, 127, 80)
    my_turtle.penup()
    my_turtle.goto(-300, 100)
    my_turtle.pendown()
    my_turtle.fillcolor(255, 127, 80)
    my_turtle.begin_fill()

    i: int = 0
    while i < 2:
        my_turtle.forward(600)
        my_turtle.right(90)
        my_turtle.forward(100)
        my_turtle.right(90)
        i += 1
    
    my_turtle.end_fill()
    

def sunset_four(my_turtle: Turtle, x: float, y: float) -> None:
    """Makes the fourth rectangular layer of my sunset: yellow."""
    my_turtle.speed(10)
    my_turtle.color(241, 196, 15)
    my_turtle.penup()
    my_turtle.goto(-300, 0)
    my_turtle.pendown()
    my_turtle.fillcolor(241, 196, 15)
    my_turtle.begin_fill()

    i: int = 0
    while i < 2:
        my_turtle.forward(600)
        my_turtle.right(90)
        my_turtle.forward(100)
        my_turtle.right(90)
        i += 1
    
    my_turtle.end_fill()


def ocean_one(my_turtle: Turtle, x: float, y: float) -> None:
    """Makes the first rectangular layer of my ocean: dark blue."""
    my_turtle.speed(10)
    my_turtle.color(33, 97, 140)
    my_turtle.penup()
    my_turtle.goto(150, -100)
    my_turtle.pendown()
    my_turtle.fillcolor(33, 97, 140)
    my_turtle.begin_fill()

    i: int = 0
    while i < 2:
        my_turtle.forward(150)
        my_turtle.right(90)
        my_turtle.forward(200)
        my_turtle.right(90)
        i += 1
    
    my_turtle.end_fill()
    

def ocean_two(my_turtle: Turtle, x: float, y: float) -> None:
    """Makes the second rectangular layer of my ocean: light blue."""
    my_turtle.speed(10)
    my_turtle.color(52, 152, 219)
    my_turtle.penup()
    my_turtle.goto(0, -100)
    my_turtle.pendown()
    my_turtle.fillcolor(52, 152, 219)
    my_turtle.begin_fill()

    i: int = 0
    while i < 2:
        my_turtle.forward(150)
        my_turtle.right(90)
        my_turtle.forward(200)
        my_turtle.right(90)
        i += 1
    
    my_turtle.end_fill()


def beach_one(my_turtle: Turtle, x: float, y: float) -> None:
    """Makes the first rectangular layer of my beach: dark tan."""
    my_turtle.speed(10)
    my_turtle.color(237, 187, 153)
    my_turtle.penup()
    my_turtle.goto(-300, -100)
    my_turtle.pendown()
    my_turtle.fillcolor(237, 187, 153)
    my_turtle.begin_fill()

    i: int = 0
    while i < 2:
        my_turtle.forward(150)
        my_turtle.right(90)
        my_turtle.forward(200)
        my_turtle.right(90)
        i += 1

    my_turtle.end_fill()


def beach_two(my_turtle: Turtle, x: float, y: float) -> None:
    """Makes the second rectangular layer of my beach: light tan."""
    my_turtle.speed(10)
    my_turtle.color(250, 229, 211)
    my_turtle.penup()
    my_turtle.goto(-150, -100)
    my_turtle.pendown()
    my_turtle.fillcolor(250, 229, 211)
    my_turtle.begin_fill()

    i: int = 0
    while i < 2:
        my_turtle.forward(150)
        my_turtle.right(90)
        my_turtle.forward(200)
        my_turtle.right(90)
        i += 1

    my_turtle.end_fill()


def house_base(my_turtle: Turtle, x: float, y: float) -> None:
    """Makes the base sqaure layer of my beach house: dark red."""
    my_turtle.speed(10)
    my_turtle.color(160, 64, 0)
    my_turtle.penup()
    my_turtle.goto(-200, -200)
    my_turtle.pendown()
    my_turtle.fillcolor(160, 64, 0)
    my_turtle.begin_fill()

    i: int = 0
    while i < 2:
        my_turtle.forward(100)
        my_turtle.right(90)
        my_turtle.forward(100)
        my_turtle.right(90)
        i += 1

    my_turtle.end_fill()


def house_roof(my_turtle: Turtle, x: float, y: float) -> None:
    """Makes the roof triangluar layer of my beach hosue: brown."""
    my_turtle.speed(10)
    my_turtle.color(120, 66, 18)
    my_turtle.penup()
    my_turtle.goto(-200, -200)
    my_turtle.pendown()
    my_turtle.fillcolor(120, 66, 18)
    my_turtle.begin_fill()

    i: int = 0
    while i < 3:
        my_turtle.forward(100)
        my_turtle.left(120)
        i += 1

    my_turtle.end_fill()


def boat(my_turtle: Turtle, x: float, y: float) -> None:
    """Makes the main layer of my boat: wood brown."""
    my_turtle.speed(5)
    my_turtle.color(125, 102, 8)
    my_turtle.penup()
    my_turtle.goto(100, -200)
    my_turtle.pendown()
    my_turtle.fillcolor(125, 102, 8)
    my_turtle.begin_fill()
    my_turtle.forward(100)
    my_turtle.right(120)
    my_turtle.forward(50)
    my_turtle.right(60)
    my_turtle.forward(75)
    my_turtle.right(60)
    my_turtle.forward(50)

    my_turtle.end_fill()


def sun_one(sun_turtle: Turtle, x: float, y: float, radius: int) -> None:
    """Makes the randomized layer of my sun in a fun and creative way: yellow."""
    sun_turtle.speed(10)
    sun_turtle.penup()
    sun_turtle.goto(x, y)
    sun_turtle.pendown()
    sun_turtle.pencolor(203, 67, 53)
    sun_turtle.begin_fill()
    sun_turtle.fillcolor(249, 231, 159)
    sun_turtle.circle(radius)
    sun_turtle.end_fill()
    sun_turtle.penup()
    sun_turtle.goto(x, y + radius)


def sun_two(sun_turtle: Turtle, x: float, y: float, radius: int) -> None:
    """Makes the randomized layer of my sun in a fun and creative way: yellow."""
    sun_turtle.speed(10)
    sun_turtle.penup()
    sun_turtle.goto(x, y)
    sun_turtle.pendown()
    sun_turtle.pencolor(40, 116, 166)
    sun_turtle.begin_fill()
    sun_turtle.fillcolor(249, 231, 159)
    sun_turtle.circle(radius)
    sun_turtle.end_fill()
    sun_turtle.penup()
    sun_turtle.goto(x, y + radius)


if __name__ == "__main__":
    main()