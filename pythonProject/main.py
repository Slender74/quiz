from tkinter import *
import customtkinter as ctk
import pygame
from PIL import ImageTk, Image
from questions import quiz_data
import random


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
        count = 1
        while count == 1:
            number = random.randint(1, 6)
            if number == 1:
                myimg = "1.jpg"
                count = 0

            elif number == 2:
                myimg = "2.jpg"
                count = 0
            elif number == 3:
                myimg = "3.jpg"
                count = 0
            elif number == 4:
                myimg = "4.jpg"
                count = 0
            elif number == 5:
                myimg = "5.jpg"
                count = 0
            elif number == 6:
                myimg = "6.jpg"
                count = 0
        bg = PhotoImage(file=myimg)
        my_bg = ctk.CTkLabel(win, image=bg)
        my_bg.place(x=0, y=0)

    else:
        finished_image = ctk.CTkImage(Image.open("pngtree-thunderous-congratulations-you-win-text-yellow-win-orange-vector-png-image_27237648.png"), size=(818, 360))
        image_button = ctk.CTkButton(master=win, text="", image=finished_image, fg_color="transparent")
        image_button.pack(padx=10, pady=10)
        image_button.place(x=550, y=300)





#initialize sound
pygame.mixer.init()

# System Settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#win frame
win = ctk.CTk()
win.geometry("1920x1080")
frame = Frame(win, width=1920, height=1080)

bg = PhotoImage(file="Untitled design.png")
my_bg = ctk.CTkLabel(win, image=bg)
my_bg.place(x=0, y=0)


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
    button.pack(pady=3)
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

#picture_frame = ctk.CTkImage(Image.open("Webcam.png"), size=(700, 500))
#frame_picture = ctk.CTkButton(master=win, text="", image=picture_frame, fg_color="transparent")
#frame_picture.pack(padx=1)
#frame_picture.place(x=1210, y=250)




next_btn.place(x=860, y=950)


current_question = 0

show_question()


win.resizable(0,0)
#Run app/main loop

win.mainloop()

