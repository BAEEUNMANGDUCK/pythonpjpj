from tkinter import * 
import pandas as pd
import random 


BACKGROUND_COLOR = "#B1DDC6"
try:
    words = pd.read_csv('./data/words_to_learn.csv').to_dict(orient='records')
except FileNotFoundError:
    words = pd.read_csv("./data/french_words.csv").to_dict(orient="records")

    
# french_english = [{word['French']: word["English"]} for word in words]
current_card = {}

def card_change():
    global current_card
    canvas.itemconfig(card_front, image=back_img)
    canvas.itemconfig(title, fill= "white",text="English")
    canvas.itemconfig(new_word, fill="white", text=f'{current_card["English"]}')

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words)
    canvas.itemconfig(card_front, image=front_img)
    canvas.itemconfig(title, fill='black', text='French')
    canvas.itemconfig(new_word, fill='black', text=f'{current_card["French"]}')
    flip_timer = window.after(3000, card_change)

def next_known_card():
    words.remove(current_card)
    data = pd.DataFrame(words)
    data.to_csv('./data/words_to_learn.csv', index=False)
    next_card()


window = Tk()
window.title(string="Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)



canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

right_img = PhotoImage(file='./images/right.png')
wrong_img = PhotoImage(file='./images/wrong.png')
front_img = PhotoImage(file='./images/card_front.png')
back_img = PhotoImage(file='./images/card_back.png')

# canvas create_image의 x,y 좌표의 이유 너비가 800이므로 x로 400가고, 높이가 526이므로 268 가면 정중앙으로 갈 수 있음 
card_front = canvas.create_image(400, 268, image=front_img)
title = canvas.create_text(400, 150,text="Title", font=("Ariel", 40, "italic"))
new_word = canvas.create_text(400, 263,text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
right_btn = Button(image=right_img, highlightthickness=0, command=next_known_card)
right_btn.grid(row=1, column=0)
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=1)



flip_timer = window.after(3000, card_change)
next_card()




window.mainloop()