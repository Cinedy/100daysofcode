# US STATES GAME

import pandas
import turtle
from place_state import PlaceState

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

score = 0
correct_guesses = []

while score < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Guessed", prompt="What's another state's name?").title()
    if score == 50:
        print("Congrats, you knew them all!")

    elif answer_state == "Exit":
        states_to_learn = [state for state in all_states if state not in correct_guesses]
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break

    elif answer_state in all_states:
        state_data = data[data.state == answer_state]
        x = int(state_data.x.item())
        y = int(state_data.y.item())
        if answer_state not in correct_guesses:
            correct_guesses.append(answer_state)
            score += 1
            PlaceState(answer_state, x, y)

print(f"You guessed: {correct_guesses}")
print(f"Score: {score}")



     