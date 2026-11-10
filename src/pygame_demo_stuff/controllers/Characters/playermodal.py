from dataclasses import dataclass

from src.pygame_demo_stuff.controllers.Characters.charactermodal import Character



class Player(Character):

    def action_jump(self):
        print("Jump jump")
