from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect  food
    if snake.segment[0].distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend_segment()

    # Detect collision with wall.
    if snake.segment[0].xcor() > 280 or snake.segment[0].ycor() > 280 or snake.segment[0].xcor() < -280 or \
            snake.segment[0].ycor() < -280:
        is_game_on = False
        scoreboard.end_game()

    # Detect collision with tail.
    for segment in snake.segment[1:]:
        if snake.segment[0].distance(segment) < 10:
            is_game_on = False
            scoreboard.end_game()

screen.exitonclick()
