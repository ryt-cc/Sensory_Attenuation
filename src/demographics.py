import tkinter as tk

# TO DO: Make the Ok button log everything to a csv file, including their participant number
# The goal is to have the participant number be new and go up by one with every
# new time we open the program or run an experiment, and for each demographic to be logged
# under that new entry. Id like to make it one single CSV file if possible but
# I dont know if that's possible

#--------------------------------------------------------------------------
####### SCREEN 2: DEMOGRAPHICS
#--------------------------------------------------------------------------

# Window
window = tk.Tk()
window.title("VDW Lab")
window.geometry("1280x720")
window.configure(bg = "black")

# Centering everything
main_frame = tk.Frame(window, bg="black")
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# Instructions
demo_instructions = tk.Label(
    main_frame,
    text="Please complete this information, then hit 'Ok':",
    bg="black",
    fg="#FFF5E8",
    font=("Arial", 14))
demo_instructions.pack(pady=20)


# Age box
age_frame = tk.Frame(main_frame, bg="black")
age_frame.pack(pady=10)

tk.Label(
    age_frame,
    text="Age: ",
    bg="black",
    fg="#FFF5E8",
    font=("Arial", 12)
).pack(side="left")

age_entry = tk.Entry(age_frame)
age_entry.pack(side="left")

# Gender
gender_frame = tk.Frame(main_frame, bg="black")
gender_frame.pack(pady=10)

tk.Label(
    gender_frame,
    text="Gender:",
    bg="black",
    fg="#FFF5E8",
    font=("Arial", 12)
).pack(side="left", padx=(0, 10))

gender_var = tk.StringVar(value="")
for g in ["Female", "Male", "Non binary", "Other"]:
    tk.Radiobutton(
        gender_frame,
        text=g,
        variable=gender_var,
        value=g,
        bg="black",
        fg="#FFF5E8",
        selectcolor="black",
        activebackground="black",
        activeforeground="#FFF5E8"
    ).pack(side="left", padx=5)

#Handed

hand_frame = tk.Frame(main_frame, bg="black")
hand_frame.pack(pady=10)

tk.Label(
    hand_frame,
    text="Handedness:",
    bg="black",
    fg="#FFF5E8",
    font=("Arial", 12)
).pack(side="left", padx=(0, 10))

hand_var = tk.StringVar(value="")
for h in ["Left", "Right"]:
    tk.Radiobutton(
        hand_frame,
        text=h,
        variable=hand_var,
        value=h,
        bg="black",
        fg="#FFF5E8",
        selectcolor="black",
        activebackground="black",
        activeforeground="#FFF5E8"
    ).pack(side="left", padx=5)

# Ok button
tk.Button(main_frame, text="Ok ->", font=("Arial", 12)).pack(pady=20)


window.mainloop()