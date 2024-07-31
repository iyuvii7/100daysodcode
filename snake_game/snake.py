from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for each in STARTING_POSITION:
            self.add_segments(each)

    def add_segments(self,position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def extend_snake(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for seg_numb in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_numb - 1].xcor()
            new_y = self.segments[seg_numb - 1].ycor()
            self.segments[seg_numb].goto(x=new_x, y=new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def reset(self):
        for seg in self.segments:
            seg.goto(x=1000, y=1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
