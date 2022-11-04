from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_input = screen.textinput(title="Place your bet", prompt="Pick a color: red, blue, green, yellow, purple, or orange")
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
all_turtles = []

y_pos = -70

for col in colors:
    temp_turtle = Turtle(shape="turtle")
    all_turtles.append(temp_turtle)
    temp_turtle.color(col)
    temp_turtle.penup()
    temp_turtle.goto(x=-230, y=y_pos)
    y_pos += 30

is_game_on = False

if user_input:
    is_game_on = True

while is_game_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_game_on = False
            winning_turtle = turtle.fillcolor()

            if user_input == winning_turtle:
                print(f"You've won! The {winning_turtle} turtle won")
            else:
                print(f"You've lost! The {winning_turtle} turtle won")

        random_distance = random.randint(0, 10)

        turtle.forward(random_distance)

screen.exitonclick()