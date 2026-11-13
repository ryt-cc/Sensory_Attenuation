import time

import pygame

from src.controllers.Actors.ballactor import PlayerBall
from src.controllers.Actors.baseactor import BaseActor
from src.controllers.Actors.goalactor import GoalActor
from src.controllers.games.basegame import BaseGame, GameResults, handle_events
from src.controllers.games.constants import SCREEN_SIZE
from src.controllers.screens.messagescreen import display_message_to_player
from src.helpers.message_display_helper import display_message
from src.helpers.tone_generator_helper import make_beep
from src.messages.sample_game_messages import SAMPLE_GAME_MESSAGE_1, SAMPLE_GAME_WELCOME

## All actors in this list will be added to screen with correct logic based on key
#
actor_dict = {
    GoalActor: pygame.Rect(0, 0, 20, SCREEN_SIZE[1]),
    PlayerBall: (SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2)
}


class SampleGame(BaseGame):
    def __init__(self):
        super().__init__()
        self.players = []
        self.npcs = []
        self.rounds_counter = 0

    def build_actor_list(self) -> None:
        for key, value in actor_dict.items():
            if issubclass(key, PlayerBall):
                self.players.append(PlayerBall())
                self.players[-1].jump_to(value)
            if issubclass(key, GoalActor):
                self.npcs.append(GoalActor(value))

    def draw_actors(self) -> None:
        for _actor in self.players:
            if isinstance(_actor, PlayerBall):
                pygame.draw.circle(self.screen, "blue", _actor.rect.center, _actor.radius)
        for _actor in self.npcs:
            if isinstance(_actor, GoalActor):
                pygame.draw.rect(self.screen, "red", _actor.rect)

    def calculate_score(self) -> int:
        current_time = time.time_ns() // 1_000_000
        completed_time = current_time - self.start_time
        self.start_time = current_time
        return completed_time

    def start(self, number_of_rounds_to_play: int):
        run_counter = 0
        self.window_setup()
        self.set_clock()
        self.build_actor_list()
        self.start_time = time.time_ns() // 1_000_000
        _display_message:bool = False
        while run_counter < number_of_rounds_to_play:
            beep_volume = 10.0
            event = handle_events()
            match event:
                case 10:
                    if not _display_message:
                        _display_message = True
                        message = SAMPLE_GAME_MESSAGE_1
                    else:
                        _display_message = False

            for actor in self.players:
                actor.move()
            for actor in self.npcs:
                if isinstance(actor, GoalActor):
                    collided_player = actor.detect_player(self.players)
                    if collided_player:
                        collided_player.reset_drag()
                        beep = make_beep(frequency=440, duration_ms=300,volume=beep_volume)
                        beep.play()
                        collided_player.reset_ball_to_random_y_location(1000)

                        print(f"Trial {self.rounds_counter} Time to complete : {self.calculate_score()}ms")
                        print(f"Beep volume : {beep_volume}\n")
                        run_counter += 1



            self.screen.fill("black")
            if _display_message:
                text_surface,text_rect = display_message(SAMPLE_GAME_MESSAGE_1)
                self.screen.blit(text_surface, text_rect)

            self.draw_actors()
            pygame.display.flip()  # Refresh on-screen display
            self.clock.tick(240)  # wait until next frame (at 60 FPS)


if __name__ == '__main__':
    # Game closes after 3 rounds completed
    results  = display_message_to_player("message", SAMPLE_GAME_WELCOME)
    if results:
        number_of_rounds_to_play = 3
        SampleGame().start(number_of_rounds_to_play)
