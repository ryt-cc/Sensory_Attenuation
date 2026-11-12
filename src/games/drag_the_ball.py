from abc import ABC

import pygame
from pygame import Event

from src.games.modals.base_game_modal import BaseGame
from src.games.modals.resultsmodal import GameResults


class DragTheBallGame(BaseGame):

    def keyrelease_event_handler(self, event: Event):
        pass

    def mouse_motion_event_handler(self, event: Event):
        pass

    def mouse_press_event_handler(self, event: Event):
        pass

    def mouse_release_event_handler(self, event: Event):
        pass

    def keypress_event_handler(self, event: Event):
        pass

    def create_player(self):
        self.player = pygame.Rect(0,0,20,20)
        pygame.draw.circle(self.screen, "blue", self.player.center, 30)

    def start(self) -> None:
        self.window_setup()
        self.set_clock()
        while True:
            # Process Actors inputs.
            self.handle_events()



    def collect_results(self) -> GameResults:
        print("We got the score")
        return GameResults(
            sample_id = 1,
            name_of_game = "drag the ball",
            rounds = 3,
            score = 100
        )

if __name__ == '__main__':
    DragTheBallGame().start()