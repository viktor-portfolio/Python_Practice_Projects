from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
ORIGINAL_PATH = "data/french_words.csv"
WORDS_TO_LEARN_PATH = "data/words_to_learn.csv"

get_current_card = {}
try:
    data = pandas.read_csv(WORDS_TO_LEARN_PATH)
except FileNotFoundError:
    original_data = pandas.read_csv(ORIGINAL_PATH)
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")

def got_it_right():
    data_dict.remove(get_current_card)
    data_frame = pandas.DataFrame(data_dict)
    data_frame.to_csv(WORDS_TO_LEARN_PATH, index=False)
    get_random_word()


def get_random_word():
    global get_current_card, flip_timer
    window.after_cancel(flip_timer)
    get_current_card = random.choice(data_dict)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text,text=get_current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=front_card)
    flip_timer = window.after(3000, func=switch_to_english)


def switch_to_english():
    canvas.itemconfig(canvas_image, image=back_card)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=get_current_card["English"], fill="white")


# ________________________ UI ________________________ #
window = Tk()
window.title("Flash Card")
window.config(padx=50,pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=switch_to_english)

front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800,height=526, background=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400,263,image=front_card)
title_text = canvas.create_text(400, 150, text="",font=("Times New Roman",40, "italic"))
word_text = canvas.create_text(400,263, text="", font=("Times New Roman",60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


right_button = Button(image=right_image, highlightthickness=0, command=got_it_right)
right_button.grid(column=0, row=1)

wrong_button = Button(image=wrong_image, highlightthickness=0, command=get_random_word)
wrong_button.grid(column=1, row=1)

get_random_word()

window.mainloop()