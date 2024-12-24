from turtle import Turtle


MOVE_SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.prev_seg_pos = []
        self.body_pos = (0.0, 0.0)
        self.create_snake()
        self.head = self.segments[0]
        self.paused = True

    def create_snake(self):
        for snakeSegment in range(3):
            self.add_segment()

    def add_segment(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        if len(self.segments) > 0:
            segment_pos_x = self.segments[-1].pos()[0] - 20
            segment_pos_y = self.segments[-1].pos()[1]
            new_segment.goto(segment_pos_x, segment_pos_y)
        else:
            new_segment.goto(0,0)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.paused = True

    def unpause(self):
        self.paused = False

    def move(self):
        if not self.paused:
            for segment in self.segments:
                if self.segments.index(segment) == 0:
                    self.prev_seg_pos.append(segment.pos())
                    segment.forward(MOVE_SPEED)
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
