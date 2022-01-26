from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake_Game")
screen.tracer(0) # Turn turtle animation off


snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

game_is_one = True

while game_is_one:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.make_new_food()
        snake.extend_snake()
        score.increase_score()


    #Detect collision with the wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        score.game_over()
        game_is_one = False


    #Detect collision with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_one = False
            score.game_over()




screen.exitonclick()