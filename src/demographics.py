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

age_label = tk.Label(
    age_frame,
    text="Age: ",
    bg="black",
    fg="#FFF5E8",
    font=("Arial", 12))
age_label.pack(side="left")

age_entry = tk.Entry(age_frame)
age_entry.pack(side="left")

# Gender
gender_frame = tk.Frame(main_frame, bg="black")
gender_frame.pack(pady=10)

gender_label = tk.Label(
    gender_frame,
    text="Gender:",
    bg="black",
    fg="#FFF5E8",
    font=("Arial", 12))

gender_label.pack(side="left", padx=(0, 10))

gender_var = tk.StringVar(value="None")
for each_gender in ["Female", "Male", "Non binary", "Other"]:
    gender_button = tk.Radiobutton(
        gender_frame,
        text=each_gender,
        variable=gender_var,
        value=each_gender,
        bg="black",
        fg="#FFF5E8",
        selectcolor="black",
        activebackground="black",
        activeforeground="#FFF5E8")

    gender_button.pack(side="left", padx=5)

#Handed

hand_frame = tk.Frame(main_frame, bg="black")
hand_frame.pack(pady=10)

hand_label = tk.Label(
    hand_frame,
    text="Are you left or right handed?:",
    bg="black",
    fg="#FFF5E8",
    font=("Arial", 12)
)
hand_label.pack(side="left", padx=(0, 10))

hand_var = tk.StringVar(value="None")

for each_hand in ["Left", "Right"]:
    hand_button = tk.Radiobutton(
        hand_frame,
        text=each_hand,
        variable=hand_var,
        value=each_hand,
        bg="black",
        fg="#FFF5E8",
        selectcolor="black",
        activebackground="black",
        activeforeground="#FFF5E8")

    hand_button.pack(side="left", padx=5)


# Ok button
tk.Button(main_frame, text="Ok ->", font=("Arial", 12)).pack(pady=20)


window.mainloop()