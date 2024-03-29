from email.mime import image
import turtle
from tkinter import messagebox
import pandas as pd
data = pd.read_csv("day 25\\day-25-us-states-game-start\\50_states.csv")
stateList = data.state.tolist()
screen = turtle.Screen()
screen.title("US States")
image = "day 25\\day-25-us-states-game-start\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
answerList = []
answerCount = 0
while answerCount < 50:
    answerCount = len(answerList)
    answer = str(screen.textinput(
        title=f"Guess the state{answerCount}/50", prompt="Name the state")).title()
    if answer == "Exit":
        break
    elif answer in answerList:
        t = turtle.Turtle()
        messagebox.showinfo(title="Error", message="Enter a New State Name!")
    elif answer not in stateList:
        t = turtle.Turtle()
        messagebox.showinfo(title="Error", message="Enter a Valid State Name!")
    elif answer == "exit":
        break
    else:
        answerList.append(answer)
        state_data = data[data["state"] == answer]
        print(state_data)
        loc_x = int(data[data.state == answer].x.values[0])
        loc_y = int(data[data.state == answer].y.values[0])
        answers = turtle.Turtle()
        answers.hideturtle()
        answers.penup()
        answers.goto(loc_x, loc_y)
        answers.write(answer)
missingState = []
missingState = [state for state in stateList if state not in answerList]
# for state in stateList:
#     if state not in answerList:
#         missingState.append(state)
df = pd.DataFrame(missingState)
df.to_csv("day 25\\day-25-us-states-game-start\\missingstates.csv")
screen.exitonclick()
