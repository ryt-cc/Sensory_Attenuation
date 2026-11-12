import time

import pygame

from src.controllers.Actors.ballactor import PlayerBall
from src.controllers.Actors.baseactor import BaseActor
from src.controllers.Actors.goalactor import GoalActor
from src.controllers.games.basegame import BaseGame, GameResults, handle_events
from src.controllers.games.constants import SCREEN_SIZE
from src.helpers.tone_generator_helper import make_beep

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

    def calculate_score(self) -> GameResults:
        pass

    def start(self, number_of_rounds_to_play: int):
        run_counter = 0
        game = SampleGame()
        game.window_setup()
        game.set_clock()
        game.build_actor_list()
        game.start_time = time.time_ns() // 1_000_000
        while run_counter < number_of_rounds_to_play:
            handle_events()

            for actor in game.players:
                actor.move()
            for actor in game.npcs:
                if isinstance(actor, GoalActor):
                    collided_player = actor.detect_player(game.players)
                    if collided_player:
                        collided_player.reset_drag()
                        beep = make_beep(frequency=440, duration_ms=500)
                        beep.play()
                        collided_player.reset_ball_to_random_y_location(1000)
                        current_time = time.time_ns() // 1_000_000
                        print(f"Trial {run_counter} Time to complete : {current_time - game.start_time}ms")
                        game.start_time = current_time
                        run_counter += 1

            game.screen.fill("black")
            game.draw_actors()
            pygame.display.flip()  # Refresh on-screen display
            game.clock.tick(240)  # wait until next frame (at 60 FPS)


if __name__ == '__main__':
    # Game closes after 3 rounds completed
    number_of_rounds_to_play = 3
    SampleGame().start(number_of_rounds_to_play)
