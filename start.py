from tkinter import *
import customtkinter as ctk
import main

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

win2 = ctk.CTk()
win2.geometry("1920x1080")

win2.iconbitmap("anime-manga-word-text-tony-rubino-transparent-_1_.ico")
win2.title("Anime Quiz")




start_button = ctk.CTkButton(
    win2,
    text="Start",
    fg_color="transparent",
    font=("Bahnschrift Condensed", 100),
    anchor=CENTER,

)

start_button.pack(padx=10, pady=10)
start_button.place(x=850, y=450)


setting_button = ctk.CTkButton(
    win2,
    text="Settings",
    fg_color="transparent",
    font=("Bahnschrift Condensed", 100),
    anchor=CENTER
)
setting_button.pack(padx=10, pady=10)
setting_button.place(x=810, y=600)


label = ctk.CTkLabel(
    win2,
    text="Anime Quiz",
    fg_color="transparent",
    font=("Bahnschrift Condensed", 100),
    anchor=CENTER
)
label.pack(padx = 10, pady=10)




win2.mainloop()