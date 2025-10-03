#FLASHCARD APP

from tkinter import *
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"

to_learn = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def create_flashcard():
        global card, flip_timer
        window.after_cancel(flip_timer)
        card = choice(to_learn)
        canvas.itemconfig(card_title, fill="black", text="German")
        canvas.itemconfig(card_text, fill="black", text=(card["German"]))
        canvas.itemconfig(canvas_img, image=front_img)
        flip_timer = window.after(3000, flip_card)
        
def flip_card():
        canvas.itemconfig(canvas_img, image=back_img)
        canvas.itemconfig(card_title, fill="white", text="English")
        canvas.itemconfig(card_text, fill="white", text=(card["English"]))

#When word is known:
def remove_word():
    to_learn.remove(card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    create_flashcard()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="German", fill="black", font=("Ariel", 40, "italic"))
card_text = canvas.create_text(400, 263, text="Ich", fill="black", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

#buttons
right_image = PhotoImage(file="images/right.png")
right = Button(image=right_image, bg=BACKGROUND_COLOR, command=remove_word)
right.grid(column=1, row=1)
wrong_image = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_image, bg=BACKGROUND_COLOR, command=create_flashcard)
wrong.grid(column=0, row=1)

create_flashcard()
window.mainloop()

