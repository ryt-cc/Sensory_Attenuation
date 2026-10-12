import tkinter as tk

#---------------------------------------------------------------------------
####### PROMPT BEFORE RECORDED FOCUS TASK
#---------------------------------------------------------------------------


# Window
window = tk.Tk()
window.title("VDW Lab")
window.geometry("1280x720")
window.configure(bg = "black")

# Intro
auto_prompt = tk.Label(
    window,
    text = "You have completed the practice run! \n"
           "When you are ready to begin the actual task, please click 'Ok'.",
    bg = "black",
    fg = "#FFF5E8",
    font = ("Arial", 14))
auto_prompt.place(relx=0.5, rely=0.5, anchor="center")

# Next button
btn = tk.Button(
    window,
    text = "Ok ->",
    font = ("Arial", 12))
btn.place(relx=0.5, rely=0.60, anchor="center")

window.mainloop()