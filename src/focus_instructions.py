import tkinter as tk

# TO DO: Create the actual instructions

#---------------------------------------------------------------------------
####### SCREEN 10 INSTRUCTIONS FOR FOCUS TASK
#---------------------------------------------------------------------------

# Window
window = tk.Tk()
window.title("VDW Lab")
window.geometry("1280x720")
window.configure(bg = "black")

# Intro
focus_instructions = tk.Label(
    window,
    text = "The instructions for the focus task will go here. \n"
           "We will begin with a practice run, which will be completed twice. \n"
           "When you are ready to begin the practice run, please click 'Ok'.",
    bg = "black",
    fg = "#FFF5E8",
    font = ("Arial", 14))
focus_instructions.place(relx=0.5, rely=0.5, anchor="center")

# Next button
btn = tk.Button(
    window,
    text = "Ok ->",
    font = ("Arial", 12))
btn.place(relx=0.5, rely=0.60, anchor="center")

window.mainloop()