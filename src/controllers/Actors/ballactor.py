import random

import pygame.mouse

from src.controllers.Actors.baseactor import BaseActor
from src.controllers.Actors.playerbaseactor import PlayerBase
from src.controllers.games.constants import SCREEN_SIZE


class PlayerBall(PlayerBase):
    drag_start:bool
    radius = 20
    def __init__(self):
        self.rect = pygame.Rect(0,0,40, 40)
        self.collision_box = pygame.Rect(0,0,20,20)
        self.drag_start = False

    def move(self) -> None:
        """Allows dragging of ball with mouse pointer"""
        if not self.drag_start:
            if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                self.drag_start = True
                pygame.mouse.set_visible(False)

        if self.drag_start:
            if not pygame.mouse.get_pressed()[0]:
                self.drag_start = False
                pygame.mouse.set_visible(True)
                return
            self.previous_location = self.rect.center
            self.rect.center = pygame.mouse.get_pos()
            self.collision_box.center = self.rect.center
            self.keep_inside_screen()

    def reset_drag(self) -> None:
        self.drag_start = False
        pygame.mouse.set_visible(True)

    def reset_ball_to_random_y_location(self,spawn_line:int) -> None:
        """Reset the ball to a given X coordinate but random Y"""

        self.rect.x = spawn_line
        self.rect.y = random.randint(10,SCREEN_SIZE[1]-10)
        self.collision_box.center = self.rect.center



