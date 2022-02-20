from turtle import  Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]  # The start position of the snake's segments
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    segments = [] #A segments of the snake

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION: # Create the snake
            self.add_segment(position)


    def add_segment(self,position):
        #Here add to the segments list a new snake's segment
        new_segments = Turtle(shape="square")
        new_segments.color("white")
        new_segments.penup()
        new_segments.goto(position)
        self.segments.append(new_segments)


    def extend_snake(self):
        #Add to stegment's list a new stegment with the position of the tail
        self.add_segment(self.segments[-1].position())


    def move(self):
        #In this loop i move the snake
        #First move the tail of the snake to the "middle" of the body
        #Second move the "middle" of the cidy to the head's place
        #And THE head move forward
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)


    def reset(self):
        for seg in self.segments: #after the player lost the snake move out of screen
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]



