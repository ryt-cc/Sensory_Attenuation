import tkinter as tk

#---------------------------------------------------------------------------
####### EXPERIMENT COMPLETE
#---------------------------------------------------------------------------

def end_window():
    # Window
    window = tk.Tk()
    window.title("VDW Lab")
    window.geometry("1280x720")
    window.configure(bg="black")

    # Intro
    experiment_complete = tk.Label(
        window,
        text="You've completed the experiment! Please let the experimentor know. \n"
             "If you're a student completing this for class credit, your credit will be updated within x hours.",
        bg="black",
        fg="#FFF5E8",
        font=("Arial", 14))
    experiment_complete.place(relx=0.5, rely=0.5, anchor="center")
    #Creates a next button
    next_button = tk.Button(window, text="NEXT", command=window.destroy)
    #adds button to existing window
    next_button.pack(pady=10)
    #starts loop for this window
    window.mainloop()


if __name__ == '__main__':
    end_window()
