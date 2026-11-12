import tkinter as tk
from symtable import Function
from time import sleep
from tkinter import Tk, Frame, ttk, IntVar
from typing import Optional

class TkWindowHelper:
    root_window:tk.Tk
    next_pressed:bool = False
    main_text_id = None
    instructions:list
    next_commands:list[Function]
    message_counter = 0
    test_results = []
    perceived_volume : tk.IntVar
    def __init__(self):

        self.root_window = tk.Tk()
        # Set the initial window size (Width x Height) and updates object
        # so we can get the window size later
        # self.root_window.geometry("1280x720") # set window size
        self.root_window.state('zoomed') # make the window full screen
        self.root_window.attributes('-topmost', True) # brings the window to the front
        self.root_window.focus_force() # sets window as focus
        self.root_window.update_idletasks() # applies changes



    def setup_genric_window(
            self,
            instructions:list[str],
            window_bg_color:Optional[str] = "black"
    ) -> None:
        """Creates a generic TK window

        :parameter instructions:list[str],
        :parameter window_bg_color:Optional[str]
        """
        #easy way to set colors
        self.instructions = instructions
        text_color = "white"
        text_background_color = "black"
        button_frame_background_color = "green"
        text_box_height_percentage = .7 # .7 is 70% of total window will be textbox

        def next_was_pressed() -> None:
            self.next_pressed = True
            self.message_counter += 1
            if self.message_counter < len(self.instructions):
                text_canvas.itemconfig(
                    self.main_text_id,
                    text=self.instructions[self.message_counter]
                )
            else:
                self.root_window.destroy()
        def previous_was_pressed() -> None:
            self.next_pressed = True
            self.message_counter -= 1
            if self.message_counter < len(self.instructions):
                text_canvas.itemconfig(
                    self.main_text_id,
                    text=self.instructions[self.message_counter]
                )
        def submit_button_pressed()->None:
            self.test_results.append(self.perceived_volume.get())
            slider.set(0)


        content = tk.Frame(self.root_window)
        content.pack(fill="both", expand=True)
        self.root_window.update_idletasks()
        content.columnconfigure(0,weight=1)
        # content.columnconfigure(1, weight=1)
        content.rowconfigure(0, weight=1)
        #height is the total window height * text_box_height_percentage
        text_canvas = tk.Canvas(
            content,
            bg=text_background_color
        )
        #adds text_canvas to content frame
        text_canvas.grid(row=0,column=0,columnspan=5,sticky="nsew")


        #create canvas for buttons
        button_frame = tk.Frame(
            content,
            bg=button_frame_background_color
        )
        button_frame.grid(row=0, column=6,sticky="ne")

        # Create previous button
        # when pressed application window is closed
        previous_button = tk.Button(
            button_frame,
            text="Previous",
            command=previous_was_pressed,
            bd=0,
            padx=50,
            pady=50
        )

        # Create next button
        # when pressed application window is closed
        next_button = tk.Button(
            button_frame,
            text="Next",
            command=next_was_pressed,
            bd=0,
            padx=50,
            pady=50
        )

        # Create start button
        # when pressed application window is closed
        start_button = tk.Button(
            button_frame,
            text="Submit",
            command=submit_button_pressed,
            bd=0,
            padx=50,
            pady=50
        )

        # Add button to window
        previous_button.grid(row=1,column=0,sticky="ew")
        next_button.grid(row=0,column=0,sticky="ew")
        start_button.grid(row=2,column=0,sticky="ew")
        self.root_window.update_idletasks()

        #adds text to text_canvas
        # centers text to half the width and height of the text_canvas
        self.main_text_id = text_canvas.create_text(
            text_canvas.winfo_width()/2,
            text_canvas.winfo_height()/2,
            text=self.instructions[0],
            fill=text_color,
            font=("Courier", 20)
        )
        slider = self.add_volume_slider(button_frame)




    def add_volume_slider(self,button_frame:tk.Frame) -> tk.Scale:
        """
        Creates a generic window for data collection
        Has sliders to capture perceived volume\n
        :parameter button_frame:tk.Frame
        :return: slider:tk.Scale
        """
        def on_slide(value):
            # The current value is automatically passed as a string to the command function
            label.config(text=f"Value: {value}")
            self.perceived_volume.set(round(slider.get()))


        #Creates a new root using our generic window function
        #Creates a new volume slider
        slider = tk.Scale(
            button_frame,
            from_=0,
            to=100,
            orient="vertical",  # Can also be tk.VERTICAL
            command=on_slide,  # Callback function called when the slider moves
            length=500,
            width=50
        )
        #Adds slider to button frame
        slider.grid(column=0,row=4,padx=50,sticky="nsew")

        # Create a label to display the current slider value
        label = tk.Label(button_frame, text="Value: 0", font=("Arial", 14))

        #Creates a variable to save our results in
        self.perceived_volume = tk.IntVar(value=0)

        return  slider

def results_window(results:list[str]) -> None:
    root = tk.Tk()
    root.title("results")
    root.geometry("200x200")
    root.attributes('-fullscreen', False)
    root.attributes('-topmost', True)
    root.focus_force()
    root.eval('tk::PlaceWindow . center')
    # Create the canvas widget
    canvas = tk.Canvas(root,bg="black")
    canvas.pack(expand=True,fill="both")
    display_string = f"{results[0]}"
    for result in results:
        display_string += f" ,{result}"
    # Draw text onto the canvas
    canvas.create_text(
        100, 100,
        text=f"Results:\n{display_string}",
        fill="white",
        font=("Helvetica", 16, "bold")
    )

    root.mainloop()



if __name__ == '__main__':
    instructions = ["sample Text", "You just hit next", "There ya go, did it again", "Im sleepy", "Goodbye"]
    x = TkWindowHelper()
    x.setup_genric_window(instructions=instructions)
    x.root_window.mainloop()
    print(x.test_results)
    results_window(x.test_results)







