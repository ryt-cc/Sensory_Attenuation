import tkinter as tk

#--------------------------------------------------------------------------
####### SCREEN 1: OPEN WINDOW + INTRO
#--------------------------------------------------------------------------

# Window
window = tk.Tk()
window.title("Sensory Attenuation Experiment")
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

# Check box for agree and disagree. If disagree, skip to last screen saying thank you after clicking next.
# Going to the next page needs to log their entries on the spreadsheet

#---------------------------------------------------------------------------
####### SCREEN 4: INSTRUCTIONS FOR AUTOMATIC TASK
#---------------------------------------------------------------------------

auto_instructions = tk.Label(
    window, 
    text = "Instructions will go here. Moving a ball back and forth from target to target.")
auto_instructions.pack()

# They'll click right and drag left into the target spot, let go and it disappears and starts the next one.
# Possible to make moving from one task to the next a little smooth? I dont want anything jarring or immediately flashing.
# I feel like it's better that everything goes smooth for a natural feel to prevent jarring the attention.
# When I was a participant, the tasks I did felt abrupt and weird, and they weren't attention tasks.
# Sound user design.

#---------------------------------------------------------------------------
####### SCREEN 5 AUTOMATIC TASK PRACTICE PROMPT
#---------------------------------------------------------------------------

auto_practice_prompt = tk.Label(
    window, 
    text = "Let's complete two practice runs. After two are completed, you will then proceed to the task.")
auto_practice_prompt.pack()

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
    text = "During each task, you heard a beeping sound. Please move the slider to match how loud the sound was to you.")
auto_sound_measure.pack()

# Slider
# A 0-100 scale seems better to me because it may encourage the person to be as accurate as possible.

#---------------------------------------------------------------------------
####### SCREEN 10 INSTRUCTIONS FOR ANALYTIC TASK
#---------------------------------------------------------------------------

analytic_instructions = tk.Label(
    window, 
    text = "Instructions will go here. Dragging a ball from right to left into the target")
analytic_instructions.pack()

#---------------------------------------------------------------------------
####### SCREEN 11 ANALYTIC TASK PRACTICE PROMPT
#---------------------------------------------------------------------------

analytic_practice_prompt = tk.Label(
    window, 
    text = "Let's complete two practice runs. After two are completed, you will then proceed to the task.")
analytic_practice_prompt.pack()

#---------------------------------------------------------------------------
####### SCREEN 12 ANALYTIC TASK PRACTICE USER
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
####### SCREEN 13 ANALYTIC TASK RECORDED PROMPT
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
####### SCREEN 14 ANALYTIC TASK RECORDED USER
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
####### SCREEN 15 ANALYTIC SOUND MEASURE
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
####### SCREEN 16 "Thanks. If you're a student completing this for class credit, 
################# your credit will be updated within x hours."

window.mainloop()