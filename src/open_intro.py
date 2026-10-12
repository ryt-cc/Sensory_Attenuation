import tkinter as tk

## TO DO: Make this go to the demographics page

#--------------------------------------------------------------------------
####### SCREEN 1: OPEN WINDOW + INTRO
#--------------------------------------------------------------------------

# Window
window = tk.Tk()
window.title("VDW Lab")
window.geometry("1280x720")
window.configure(bg = "black")

# Intro
intro = tk.Label(
    window,
    text = "Please press 'Ok' to begin the experiment.",
    bg = "black",
    fg = "#FFF5E8",
    font = ("Arial", 14))
intro.place(relx=0.5, rely=0.5, anchor="center")

# Next button
btn = tk.Button(
    window,
    text = "Ok ->",
    font = ("Arial", 12))
btn.place(relx=0.5, rely=0.55, anchor="center")

window.mainloop()