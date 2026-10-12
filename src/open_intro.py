import tkinter as tk

#--------------------------------------------------------------------------
####### SCREEN 1: OPEN WINDOW + INTRO
#--------------------------------------------------------------------------

# Window
window = tk.Tk()
window.title("src")
window.geometry("400x250")
window.configure(bg = "#EEC6C6")

# Heading
title = tk.Label(
    window,
    text = "Does it need a title?")
title.pack()

# Intro
intro = tk.Label(
    window,
    text = "This is an experiment blah blah blah doing things?")
intro.pack()