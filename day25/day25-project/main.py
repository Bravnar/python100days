import turtle
import pandas as pd
from state import State
from tracker import Tracker

IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Games")
screen.setup(725, 491)
screen.bgpic(IMAGE)

tracker = Tracker()
states_df = pd.read_csv("50_states.csv")
valid_states = states_df.state.to_list()
placed_states = []

while tracker.count < 50:
    answer_state = screen.textinput(title="Guess the State", prompt="Enter a state name:").title()
    if answer_state in valid_states and answer_state not in placed_states:
        new_state = State(answer_state)
        row = states_df[states_df.state == answer_state]
        coords = (row.x.item(), row.y.item())
        new_state.slide_state(coords)
        placed_states.append(answer_state)
        tracker.incrCount()
    elif (answer_state in placed_states):
        print("You already answered that!")
    else:
        print("Wrong state!")

print("Congrats you win!")

turtle.mainloop()