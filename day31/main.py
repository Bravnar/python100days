from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
DELAY = 3000


# ------------------- DATA MANAGEMENT ---------------------#

try:
    to_learn = pd.read_csv("data/words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    to_learn = pd.read_csv("data/french_words.csv").to_dict(orient="records")
except pd.errors.EmptyDataError:
    print("You learned all the words, Resetting!")
    to_learn = pd.read_csv("data/french_words.csv").to_dict(orient="records")
    
current_card = {}

# ------------------- BUTTONS ----------------------#

def all_done():
    canvas_card.itemconfig(title, text="All words learned!", fill="white")
    canvas_card.itemconfig(word, text=f"Congratulations!", fill="white")
    canvas_card.itemconfig(canvas_image, image=card_back)

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    try:
        current_card = random.choice(to_learn)
    except IndexError:
        all_done()
        return
    canvas_card.itemconfig(title, text="French", fill="black")
    canvas_card.itemconfig(word, text=f"{current_card['French']}", fill="black")
    canvas_card.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(DELAY, flip_card)

def wrong_button():
    next_card()

def right_button():
    to_learn.remove(current_card)
    pd.DataFrame(to_learn).to_csv("data/words_to_learn.csv", index=False)
    next_card()
    
    

# ------------------- UI ---------------------------#

def flip_card():
    canvas_card.itemconfig(title, text="English", fill="white")
    canvas_card.itemconfig(word, text=f"{current_card['English']}", fill="white")
    canvas_card.itemconfig(canvas_image, image=card_back)

window = Tk()
window.title("French Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(DELAY, flip_card)

canvas_card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
canvas_image = canvas_card.create_image(400, 263, image=card_front)
title = canvas_card.create_text(400, 150, text='', font=LANGUAGE_FONT, fill="black")
word = canvas_card.create_text(400, 263, text='', font=WORD_FONT, fill="black")
canvas_card.grid(row=0, column=1, columnspan=2)


wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, bg=BACKGROUND_COLOR, highlightthickness=0, command=wrong_button)
wrong_button.grid(row=1, column=1, pady=20)


right = PhotoImage(file="images/right.png")
right_button = Button(image=right, bg=BACKGROUND_COLOR, highlightthickness=0, command=right_button)
right_button.grid(row=1, column=2, pady=20)

next_card()


window.mainloop()