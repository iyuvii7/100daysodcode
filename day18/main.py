import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

# fro random color
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

# Draw a spirograph
radius = 160
tim.pensize(1.4)
for _ in range(144):
    tim.circle(radius)
    tim.left(2.5)
    tim.color(random_color())


t.exitonclick()