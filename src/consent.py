import tkinter as tk

# TO DO: Fill in the consent information
# If you disagree, skip to last screen saying thank you after clicking OK.
# Clicking OK needs to log their entries on the spreadsheet

#---------------------------------------------------------------------------
####### SCREEN 3: CONSENT
#---------------------------------------------------------------------------

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
    text="Please select an option, then click 'Ok':",
    bg="black",
    fg="#FFF5E8",
    font=("Arial", 14))
demo_instructions.pack(pady=20)

# Consent buttons

consent_frame = tk.Frame(main_frame, bg="black")
consent_frame.pack(pady=10)

consent_label = tk.Label(
    consent_frame,
    text="Please select:",
    bg="black",
    fg="#FFF5E8",
    font=("Arial", 12)
)
consent_label.pack(side="left", padx=(0, 10))

consent_var = tk.StringVar(value="None")

for consent_yn in ["Agree", "Disagree"]:
    consent_button = tk.Radiobutton(
        consent_frame,
        text=consent_yn,
        variable=consent_var,
        value=consent_yn,
        bg="black",
        fg="#FFF5E8",
        selectcolor="black",
        activebackground="black",
        activeforeground="#FFF5E8")

    consent_button.pack(side="left", padx=5)


# Ok button
tk.Button(main_frame, text="Ok ->", font=("Arial", 12)).pack(pady=20)


window.mainloop()