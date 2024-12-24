from food import Food
from scoreboard import Scoreboard
from snake import Snake
from turtle import Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

game_is_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

def exit_game():
    screen.bye()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.unpause, "space")
screen.onkey(exit_game, "Escape")

game_started = False
while game_is_on:
    screen.update()
    time.sleep(.075)

    snake.move()

    # If player needs to press start
    if snake.paused:
        scoreboard.desc_to_start()
    # If player presses start and game has not started yet
    elif not snake.paused and not game_started:
        scoreboard.reset()
        game_started = True

    # Detect when colliding with food
    if snake.head.distance(food) < 20:
        scoreboard.add_score()
        snake.add_segment()
        food.refresh()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_started = False
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_started = False
            scoreboard.reset()
            snake.reset()

screen.exitonclick()