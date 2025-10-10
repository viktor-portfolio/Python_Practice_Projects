import turtle
import pandas
screen = turtle.Screen()

shakespear = turtle.Turtle()
shakespear.hideturtle()
shakespear.penup()

data = pandas.read_csv("50_states.csv")
data_state_names = data.state.to_list()
correct_guesses = []

screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 Guess the State", prompt="Input a state's name here!").title()

    if answer_state == "Exit":
        missing_states = [state for state in data_state_names if state not in correct_guesses]
        missed_states = pandas.DataFrame(missing_states, columns=["states"])
        missed_states.to_csv("missed_states.csv")
        break

    if answer_state in data_state_names:
        correct_guesses.append(answer_state)

        state_data = data[data.state == answer_state]
        x = int(state_data.x.iloc[0])
        y = int(state_data.y.iloc[0])

        shakespear.teleport(x,y)
        shakespear.write(answer_state)





