import turtle

import pandas
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# read the data
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
# Ohio = states_data[states_data.state == 'Ohio']

guessed_states =[]
# # convert the states names to lowercase
# for state in list(states_data.state):
#     states.append(state)
# print(states)

# run while loop until user guess every state name
print(len(all_states))
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct", prompt="Guess the state name ").title()
    # if user enter ( Exit ) create missing state name csv file.
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break

    # if user answer is right then locate that state onto map
    if answer_state in all_states:
        guessed_states.append(answer_state)
        tim = turtle.Turtle()
        tim.penup()
        tim.hideturtle()
        state_data = data[data.state == answer_state]
        tim.goto(x=state_data.x.item(), y=state_data.y.item())
        tim.write(f"{answer_state}")

screen.mainloop()
