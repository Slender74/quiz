from tkinter import *
import customtkinter as ctk
import pygame
from PIL import ImageTk, Image
from questions import quiz_data
import random
import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py',
    '--onefile',
    '--windowed'
])

win = ctk.CTk()
win.geometry("1920x1080")
frame = Frame(win, width=1920, height=1080)

bg = PhotoImage(file="3.png")
my_bg = ctk.CTkLabel(win, image=bg)
my_bg.place(x=0, y=0)



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
        finished_image = ctk.CTkImage(Image.open("main-qimg-33bd93f43317e850eecf28606f868f7a-lq.jfif"),size=(500, 360))
        image_button = ctk.CTkButton(master=win, text="", image=finished_image, fg_color="transparent")
        image_button.pack(padx=10, pady=10)
        image_button.place(x=100, y=300)
        pygame.mixer.music.load("Ding Sound Effect.mp3")
        pygame.mixer.music.play()


    else:
        feedback_label.configure(text="Incorrect")
        pygame.mixer.music.load("Wrong Buzzer Sound Effect.mp3")
        pygame.mixer.music.play()
        finished_image = ctk.CTkImage(Image.open("Youre a super weeb!!! (1).png"), size=(500, 360))
        image_button = ctk.CTkButton(master=win, text="", image=finished_image, fg_color="transparent")
        image_button.pack(padx=10, pady=10)
        image_button.place(x=100, y=300)
    for button in choice_btns:
        button.configure(state="disabled")
    next_btn.configure(state="normal")



def next_question():
    global current_question
    current_question += 1
    if current_question < len(quiz_data):
        show_question()
        if current_question == 0:
            bg = ctk.CTkImage(Image.open("3.png"))
            my_bg = ctk.CTkLabel(master=win, image=bg)
            my_bg.place(x=0, y=0)
        elif current_question == 1:
            bg = ctk.CTkImage("2.png")
            my_bg = ctk.CTkLabel(master=win, image=bg)
            my_bg.place(x=0, y=0)
        elif current_question == 2:
            bg = ctk.CTkImage("2.png")
            my_bg = ctk.CTkLabel(master=win, image=bg)
            my_bg.place(x=0, y=0)
        elif current_question == 3:
            bg = ctk.CTkImage("3.png")
            my_bg = ctk.CTkLabel(master=win, image=bg)
            my_bg.place(x=0, y=0)
        else:
            bg = ctk.CTkImage("3.png")
            my_bg = ctk.CTkLabel(master=win, image=bg)
            my_bg.place(x=0, y=0)


    else:
        finished_image = ctk.CTkImage(Image.open("Youre a super weeb!!!.png"), size=(1920, 1080))
        image_button = ctk.CTkButton(master=win, text="", image=finished_image, fg_color="transparent")
        image_button.pack(padx=0, pady=0)
        image_button.place(x=0, y=0)


#initialize sound
pygame.mixer.init()

# System Settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#win frame


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
num = 0
for i in range(4):
    num += 1
    button = ctk.CTkButton(
        win,
        font=("comicsans", 50),
        width=500,
        height=200,
        command=lambda i=i: check_answer(i),


    )
    button.pack(pady = 3)
    choice_btns.append(button)

feedback_label = ctk.CTkLabel(
    win,
    text="Test",
    font=("Comic_sans", 100),
    anchor=CENTER,
)
feedback_label.pack(pady=10)
feedback_label.place(x=200, y=400)


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

