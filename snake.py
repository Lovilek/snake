from turtle import Turtle

MOVE_DISTANCE = 20

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snakes = []
        coordinate = 0
        for i in range(0, 3):
            self.add_snake(position=[coordinate, 0])
            coordinate -= 20
        self.head = self.snakes[0]

    def add_snake(self, position):
        new_snake = Turtle("square")
        new_snake.color("cyan")
        new_snake.penup()
        new_snake.goto(position)
        self.snakes.append(new_snake)

    def extend(self):
        self.add_snake(self.snakes[-1].position())

    def move(self):
        for i in range(len(self.snakes) - 1, 0, -1):
            nex_x = self.snakes[i - 1].xcor()
            nex_y = self.snakes[i - 1].ycor()
            self.snakes[i].goto(nex_x, nex_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
