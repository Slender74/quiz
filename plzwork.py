import customtkinter as ctk
import pygame
from tkinter import *
from questions import quiz_data
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

win = ctk.CTk()
win.geometry("1920x1080")

win.iconbitmap("anime-manga-word-text-tony-rubino-transparent-_1_.ico")
win.title("Anime Quiz")


def start():
    frame1 = ctk.CTkFrame(win, width=1920, height=1080)
    frame1.place(x=0, y=0)

    start_button = ctk.CTkButton(
        frame1,
        text="Start",
        fg_color="transparent",
        font=("Bahnschrift Condensed", 100),
        anchor=CENTER,
        command=quiz

    )

    start_button.pack(pady=10)
    start_button.place(x=850, y=450)

    setting_button = ctk.CTkButton(
        frame1,
        text="Settings",
        fg_color="transparent",
        font=("Bahnschrift Condensed", 100),
        anchor=CENTER
    )
    setting_button.pack(padx=10, pady=10)
    setting_button.place(x=810, y=600)

    label = ctk.CTkLabel(
        frame1,
        text="Anime Quiz",
        fg_color="transparent",
        font=("Bahnschrift Condensed", 100),
        anchor=CENTER
    )
    label.pack(padx=10, pady=10)


def quiz():
    frame2 = ctk.CTkFrame(win, width=1920, height=1080)
    frame2.place(x=0, y=0)

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
            score_label.configure(text="Score: {}/{}".format(score, len(quiz_data)))
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
            finished_image = ctk.CTkImage(Image.open(
                "pngtree-thunderous-congratulations-you-win-text-yellow-win-orange-vector-png-image_27237648.png"),
                size=(818, 360))
            image_button = ctk.CTkButton(master=frame2, text="", image=finished_image, fg_color="transparent")
            image_button.pack(padx=10, pady=10)
            image_button.place(x=550, y=300)

    # initialize sound
    pygame.mixer.init()

    # Question label
    questionLabel = ctk.CTkLabel(
        frame2,
        text="Quiz",
        fg_color="transparent",
        font=("comic_sans", 50)
    )

    questionLabel.pack(padx=10, pady=10)

    # choice buttons
    choice_btns = []
    for i in range(4):
        button = ctk.CTkButton(
            frame2,
            font=("comicsans", 50),
            width=500,
            height=200,
            command=lambda i=i: check_answer(i),

        )
        button.pack(pady=3)
        choice_btns.append(button)

    feedback_label = ctk.CTkLabel(
        frame2,
        text="Test",
        anchor=CENTER,
    )
    feedback_label.pack(pady=10)

    score_label = ctk.CTkLabel(
        frame2,
        text="Score: 0/{}".format(len(quiz_data)),
        font=("Comic_Sans", 50),
        anchor=CENTER
    )

    score = 0

    score_label.place(x=100)

    next_btn = ctk.CTkButton(
        frame2,
        text="Next",
        font=("comic_sans", 50),
        width=200,
        height=100,
        command=next_question,
        state="disabled",
        anchor=CENTER

    )

    picture_frame = ctk.CTkImage(Image.open("Webcam.png"), size=(700, 500))
    frame_picture = ctk.CTkButton(master=frame2, text="", image=picture_frame, fg_color="transparent")
    frame_picture.pack(padx=1)
    frame_picture.place(x=1210, y=250)

    next_btn.place(x=860, y=950)

    current_question = 0

    show_question()

start()
# Run app/main loop
win.mainloop()
