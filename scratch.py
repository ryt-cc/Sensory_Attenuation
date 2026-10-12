import tkinter as tk

####### This file is scratch paper

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

#--------------------------------------------------------------------------
####### SCREEN 2: DEMOGRAPHICS
#--------------------------------------------------------------------------

# Instructions
demos_instructions = tk.Label(
    window, 
    text = "Please complete your demographics")
demos_instructions.pack()

# Empty box to type into for age, gender, 
# Going to the next page needs to log their entries on the spreadsheet

#---------------------------------------------------------------------------
####### SCREEN 3: CONSENT
#---------------------------------------------------------------------------

consent = tk.Label(
    window, 
    text = "Text for consenting?")
consent.pack()

# Check box for agree and disagree. If you disagree, skip to last screen saying thank you after clicking next.
# Going to the next page needs to log their entries on the spreadsheet

#---------------------------------------------------------------------------
####### SCREEN 4: INSTRUCTIONS FOR AUTOMATIC TASK
#---------------------------------------------------------------------------

auto_instructions = tk.Label(
    window, 
    text = "Instructions will go here. Moving a ball back and forth from target to target.")
auto_instructions.pack()


#---------------------------------------------------------------------------
####### SCREEN 6 AUTOMATIC TASK PRACTICE USER
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
####### SCREEN 7 AUTOMATIC TASK RECORDED PROMPT
#---------------------------------------------------------------------------

auto_recorded_prompt = tk.Label(
    window, 
    text = "You've completed the practice. When you are ready to move on, please press continue")
auto_recorded_prompt.pack()


#---------------------------------------------------------------------------
####### SCREEN 8 AUTOMATIC TASK RECORDED USER
#---------------------------------------------------------------------------

# Needs to log ?????????????????????????? What are we logging????????????????

#---------------------------------------------------------------------------
####### SCREEN 9 AUTOMATIC SOUND MEASURE
#---------------------------------------------------------------------------

auto_sound_measure = tk.Label(
    window, 
    text = "During each task, you heard a beeping sound. Please move the slider "
           "to match how loud the sound was to you.")
auto_sound_measure.pack()

# Slider

#---------------------------------------------------------------------------
####### SCREEN 10 INSTRUCTIONS FOR FOCUS TASK
#---------------------------------------------------------------------------

focus_instructions = tk.Label(
    window, 
    text = "Instructions will go here. Dragging a ball from right to left into the target")
focus_instructions.pack()

#---------------------------------------------------------------------------
####### SCREEN 11 FOCUS TASK PRACTICE PROMPT
#---------------------------------------------------------------------------

focus_practice_prompt = tk.Label(
    window, 
    text = "Let's complete two practice runs. After two are completed, you will then proceed to the task.")
focus_practice_prompt.pack()

#---------------------------------------------------------------------------
####### SCREEN 12 FOCUS TASK PRACTICE USER
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
####### SCREEN 13 FOCUS TASK RECORDED PROMPT
#---------------------------------------------------------------------------

focus_recorded_prompt = tk.Label(
    window,
    text = "You've completed the practice. When you are ready to move on, please press continue")
focus_recorded_prompt.pack()
#---------------------------------------------------------------------------
####### SCREEN 14 FOCUS TASK RECORDED USER
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
####### SCREEN 15 FOCUS SOUND MEASURE
#---------------------------------------------------------------------------

focus_sound_measure = tk.Label(
    window,
    text = "During each task, you heard a beeping sound. Please move the slider "
           "to match how loud the sound was to you.")
focus_sound_measure.pack()

#---------------------------------------------------------------------------
####### SCREEN 16 "Thanks. If you're a student completing this for class credit, 
################# your credit will be updated within x hours."

experiment_complete = tk.Label(
    window,
    text = "Thanks. If you're a student completing this for class credit, "
           "your credit will be updated within x hours.")
experiment_complete.pack()

window.mainloop()