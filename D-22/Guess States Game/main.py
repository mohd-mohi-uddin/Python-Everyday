import turtle
from pathlib import Path
import pandas
from name_board import NameBoard
from scoreboard import Scoreboard

P_PATH = Path(__file__).parent

screen = turtle.Screen()
image = P_PATH /"blank_states_img.gif"
screen.addshape(str(image))
turtle.shape(str(image))

names = NameBoard()
scoreboard = Scoreboard()

states_data = pandas.read_csv(P_PATH /"50_states.csv")

answered_states = []

while scoreboard.score < 50:

    answer_state = screen.textinput(title= f"{scoreboard.score}/50 Guessed.", prompt="What's another state name?").title()

    for state in states_data["state"]:
        if answer_state == state and answer_state not in answered_states:
            answered_states.append(answer_state)
            scoreboard.update_score()
            state_info = states_data[states_data.state == answer_state]
            x_cor = state_info.x.iloc[0]
            y_cor = state_info.y.iloc[0]
            names.write_name(x_cor,y_cor,answer_state)

screen.exitonclick()