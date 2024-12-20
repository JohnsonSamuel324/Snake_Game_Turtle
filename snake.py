from turtle import Turtle

MOVE_SPEED = 20
UP = 90
DOWN = -90
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.body_length = body_length = 3
        self.segments = segments = []
        self.prev_seg_pos = prev_seg_pos = []
        self.body_pos = body_pos = (0, 0)
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for snakeSegment in range(self.body_length):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(self.body_pos)
            new_pos = list(self.body_pos)
            new_pos[0] -= MOVE_SPEED
            self.body_pos = tuple(new_pos)
            self.segments.append(new_segment)

    def move(self):
        for segment in self.segments:
            if self.segments.index(segment) == 0:
                self.prev_seg_pos.append(segment.pos())
                segment.forward(20)
            else:
                self.prev_seg_pos.append(segment.pos())
                segment.goto(self.prev_seg_pos[0])
            if len(self.prev_seg_pos) >= 2:
                del self.prev_seg_pos[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)