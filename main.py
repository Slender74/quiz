from tkinter import *
import customtkinter as ctk
import pygame
from PIL import ImageTk, Image
from questions import quiz_data



#Functions to display current question and choices
def show_question():
    question = quiz_data[current_question]
    questionLabel.configure(text=question["question"])


    choices = question["choices"]
    for i in range(4):
        choice_btns[i].configure(text=choices[i], state="normal")

    feedback_label.configure(text="")



def check_answer(choice):
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")
    if selected_choice == question["answer"]:
        global score
        score += 1
        score_label.configure(text="Score: {}/{}".format(score,len(quiz_data)))
        feedback_label.configure(text="Correct")
        pygame.mixer.music.load("Ding Sound Effect.mp3")
        pygame.mixer.music.play()


    else:
        feedback_label.configure(text="Incorrect")
        pygame.mixer.music.load("Wrong Buzzer Sound Effect.mp3")
        pygame.mixer.music.play()
    for button in choice_btns:
        button.configure(state="disabled")
    next_btn.configure(state="normal")


def next_question():
    global current_question
    current_question += 1

    if current_question < len(quiz_data):
        show_question()
    else:
        win.destroy()





#initialize sound
pygame.mixer.init()

# System Settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#win frame
win = ctk.CTk()
win.geometry("1920x1080")
frame = Frame(win, width=1920, height=1080)
#Question label
questionLabel = ctk.CTkLabel(
    win,
    text="Quiz",
    fg_color="transparent",
    font=("comic_sans", 50)
)

questionLabel.pack(padx=10, pady=10)

#choice buttons
choice_btns = []
for i in range(4):
    button = ctk.CTkButton(
        win,
        font=("comicsans", 50),
        width=500,
        height=200,
        command=lambda i=i: check_answer(i),


    )
    button.pack(pady= 5)
    choice_btns.append(button)

feedback_label = ctk.CTkLabel(
    win,
    text="Test",
    anchor=CENTER,
)
feedback_label.pack(pady=10)

score_label = ctk.CTkLabel(
    win,
    text="Score: 0/{}".format(len(quiz_data)),
    font=("Comic_Sans", 50),
    anchor=CENTER
)

score = 0

score_label.place(x=100)

next_btn = ctk.CTkButton(
    win,
    text="Next",
    font=("comic_sans", 50),
    width=200,
    height=100,
    command=next_question,
    state="disabled",
    anchor=CENTER


)

next_btn.place(x=860, y=950)


current_question = 0

show_question()


win.resizable(0,0)
#Run app/main loop
win.mainloop()

