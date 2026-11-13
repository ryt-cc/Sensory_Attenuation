import pygame

from src.controllers.Actors.baseactor import BaseActor, MoveDirection
from src.controllers.games.constants import SCREEN_SIZE


class PlayerBase(BaseActor):
    movement_direction: MoveDirection
    collision_box = pygame.Rect
    previous_location = (0,0)

    def __init__(self,
                 name: str,
                 size: tuple[int, int]
                 ):
        super().__init__()
        self.name = name
        self.rect = pygame.Rect(0, 0, size[0], size[1])
        self.x_speed = 0
        self.y_speed = 0
        self.movement_direction = MoveDirection.STOPPED

    def move(self):
        pass

    def jump_to(self, screen_cords: tuple[int, int]):
        self.rect.x = screen_cords[0]
        self.rect.y = screen_cords[1]
        self.collision_box.center = self.rect.center

    def keep_inside_screen(self):
        if self.rect.x not in range(0,SCREEN_SIZE[0]) or self.rect.y not in range(0,SCREEN_SIZE[1]):
            self.rect.center = self.previous_location
