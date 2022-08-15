import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
bet = turtle.textinput(title="Make your bet", prompt="Which turtle will win ? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-150, -100, -50, 0, 50, 100]
all_turtles = []

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(new_turtle)

if bet:
    is_race_on = True

while is_race_on:
    winner = None
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == bet:
                print(f"You win! The {winner} turtle is the winner!")
            else:
                print(f"You lose! The {winner} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.fd(random_distance)


screen.exitonclick()
