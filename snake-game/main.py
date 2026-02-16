import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard(0)
snake = Snake()
food = Food()

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # detect collision with wall
    head_x = snake.head.xcor()
    head_y = snake.head.ycor()
    if head_x == 300 or head_x == -300 or head_y == 300 or head_y == -300:
        snake.head.forward(0)
        scoreboard.game_over()
        is_game_on = False

    # detect collision with tail
    for each_snake in snake.snakes[1:]:
        if each_snake.distance(snake.head) < 10:
            #snake.head.forward(0)
            scoreboard.game_over()
            is_game_on = False




screen.exitonclick()

