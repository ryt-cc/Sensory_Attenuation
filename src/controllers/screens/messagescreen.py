from tkinter import messagebox

import tkinter as tk


def display_message_to_player(title, message) -> bool:
    # Hide the blank root tkinter window
    root = tk.Tk()
    root.withdraw()
    # Show the message box (also available: showwarning, showerror, askyesno)
    result = messagebox.askyesno(title, message)
    root.destroy()
    return result

if __name__ == '__main__':
    display_message_to_player("message","Hello there")