from src.tk_windows.helpers.tk_window_helpers import create_instruction_window
from src.instructions.display_text import FOCUS_GAME_INSTRUCTIONS


def create_focus_instructions_window():
    window_name = "Focus Instructions"
    create_instruction_window(window_name,FOCUS_GAME_INSTRUCTIONS)


if __name__ == '__main__':
    create_focus_instructions_window()
