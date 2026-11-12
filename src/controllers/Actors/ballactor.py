import pygame.mouse

from src.controllers.Actors.baseactor import BaseActor
from src.controllers.Actors.playerbaseactor import PlayerBase


class PlayerBall(PlayerBase):
    drag_start:bool
    radius = 20
    def __init__(self):
        self.rect = pygame.Rect(0,0,40, 40)
        self.collision_box = pygame.Rect(0,0,20,20)
        self.drag_start = False

    def move(self):
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
            self.rect.center = pygame.mouse.get_pos()
            self.collision_box.center = self.rect.center

    def reset_drag(self):
        self.drag_start = False
        pygame.mouse.set_visible(True)



