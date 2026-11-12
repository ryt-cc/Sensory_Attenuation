from abc import ABC, abstractmethod

import pygame
from pygame import Surface, Clock

from src.controllers.Actors.baseactor import BaseActor
from src.controllers.Actors.playerbaseactor import PlayerBase
from src.controllers.games.constants import SCREEN_SIZE


class GameResults:
    player_id:int
    game_name:str
    results:dict



def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                raise SystemExit


class BaseGame(ABC):
    name:str
    rounds:int
    start_time:int
    end_time:int
    screen:Surface
    clock: Clock
    players: list[PlayerBase]
    npcs: list[BaseActor]

    def window_setup(self) -> None:
        self.screen = pygame.display.set_mode(SCREEN_SIZE, pygame.SCALED, vsync=1)

    def set_clock(self) -> None:
        self.clock = pygame.time.Clock()

    @abstractmethod
    def build_actor_list(self) -> None:
        """Build actor list and save to self.actors"""
    @abstractmethod
    def draw_actors(self) -> None:
        """Draws list of actors"""

    @abstractmethod
    def calculate_score(self) -> GameResults:
        """Returns results object based on game type"""

    def start(self,number_of_rounds_to_play:int) -> None:
        """Setups up game and gives controller to player"""

