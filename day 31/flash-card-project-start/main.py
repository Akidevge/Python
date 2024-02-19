from email.mime import image
import tkinter
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
window = tkinter.Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flash Card app")
global randomnum
# images
card_back = tkinter.PhotoImage(
    file=r"day 31\flash-card-project-start\images\card_back.png")
card_front = tkinter.PhotoImage(
    file=r"day 31\flash-card-project-start\images\card_front.png")
right = tkinter.PhotoImage(
    file=r"day 31\flash-card-project-start\images\right.png")
wrong = tkinter.PhotoImage(
    file=r"day 31\flash-card-project-start\images\wrong.png")
# functions


def random_word():
    global randomnum
    randomnum = random.randint(0, len(tolearn))
    canvas.itemconfig(card_img, image=card_front)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=csvdata["French"][randomnum], fill="black")
    window.after(3000, flip_card)


def flip_card():
    global randomnum
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=csvdata["English"][randomnum], fill="white")
    canvas.itemconfig(card_img, image=card_back)
# D:\Python\word_to_learn.csv


def known_word():
    currentcard = {}
    currentcard = tolearn[randomnum]
    tolearn.remove(currentcard)
    data = pd.DataFrame(tolearn)
    data.to_csv(r"day 31\flash-card-project-start\data\word_to_learn.csv")
    random_word()


# canvas
try:
    csvdata = pd.read_csv(
        r"day 31\flash-card-project-start\data\word_to_learn.csv")
except FileNotFoundError:
    csvdata = pd.read_csv(
        r"day 31\flash-card-project-start\data\french_words.csv")
canvas = tkinter.Canvas(width=800, height=526)
tolearn = csvdata.to_dict(orient="records")
card_img = canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
# buttons
right_button = tkinter.Button(
    image=right, highlightthickness=0, command=known_word)
right_button.grid(row=1, column=0)
wrong_button = tkinter.Button(
    image=wrong, highlightthickness=0, command=random_word)
wrong_button.grid(row=1, column=1)
random_word()
window.mainloop()
