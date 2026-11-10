import math
from dataclasses import dataclass
from enum import Enum

import pygame

class CharacterAction(Enum):
    def display(self):
        return "Nothing"


@dataclass
class MoveDirection(CharacterAction):
    STOPPED = 0
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4
    NORTH_EAST = 5
    NORTH_WEST = 6
    SOUTH_EAST = 7
    SOUTH_WEST = 8

class Character:
    name: str
    rect: pygame.Rect
    accel_rate = 1
    max_speed = 10
    drag = .5
    x_speed = 0
    y_speed = 0

    def __init__(self,
                 name:str,
                 size:tuple[int,int]
                 ):
        self.name = name
        self.rect = pygame.Rect(0,0,size[0],size[1])
        self.x_speed = 0
        self.y_speed = 0


    def move(self, in_direction:MoveDirection):
        # print(f"Move in direction {in_direction}")
        match in_direction.name:
            case MoveDirection.NORTH.name:
                self.y_speed -= self.accel_rate
            case MoveDirection.SOUTH.name:
                self.y_speed += self.accel_rate
            case MoveDirection.WEST.name:
                self.x_speed -= self.accel_rate
            case MoveDirection.EAST.name:
                self.x_speed += self.accel_rate
            case MoveDirection.NORTH_EAST.name:
                self.y_speed -= self.accel_rate
                self.x_speed += self.accel_rate
            case MoveDirection.NORTH_WEST.name:
                self.y_speed -= self.accel_rate
                self.x_speed -= self.accel_rate
            case MoveDirection.SOUTH_EAST.name:
                self.y_speed += self.accel_rate
                self.x_speed -= self.accel_rate
            case MoveDirection.SOUTH_WEST.name:
                self.y_speed += self.accel_rate
                self.x_speed += self.accel_rate


        self.apply_speed_limit(in_direction)
        self.rect.move_ip(self.x_speed, self.y_speed)
        # print(f"X: {self.x_speed}\nY: {self.y_speed}")
        # print(f"Accel rate: {self.accel_rate}")
        # print(f"Max speed: {self.max_speed}\n{'*'*20}")

    def jump_to(self,screen_cords:tuple[int,int]):
        self.rect.x = screen_cords[0]
        self.rect.y = screen_cords[1]

    def apply_drag(self):
        if self.x_speed > 0:
            self.x_speed -= self.drag
        elif self.x_speed < 0:
            self.x_speed += self.drag
        if self.y_speed > 0:
            self.y_speed -= self.drag
        elif self.y_speed < 0:
            self.y_speed += self.drag


    def apply_speed_limit(self, in_direction:MoveDirection):
        if in_direction in [
            MoveDirection.NORTH,
            MoveDirection.SOUTH,
            MoveDirection.EAST,
            MoveDirection.WEST
        ]:
            if self.x_speed >= self.max_speed:
                self.x_speed = self.max_speed
            elif self.x_speed <= -self.max_speed:
                self.x_speed = -self.max_speed
            if self.y_speed >= self.max_speed:
                self.y_speed = self.max_speed
            elif self.y_speed <= -self.max_speed:
                self.y_speed = -self.max_speed
        if in_direction in [
            MoveDirection.NORTH_EAST,
            MoveDirection.NORTH_WEST,
            MoveDirection.SOUTH_EAST,
            MoveDirection.SOUTH_WEST
        ]:
            if self.x_speed > math.ceil(self.max_speed / 2):
                self.x_speed = math.ceil(self.max_speed / 2)
            elif self.y_speed > math.ceil(self.max_speed / 2):
                self.y_speed = math.ceil(self.max_speed / 2)
            if self.x_speed < -math.ceil(self.max_speed / 2):
                self.x_speed = -math.ceil(self.max_speed / 2)
            elif self.y_speed < -math.ceil(self.max_speed / 2):
                self.y_speed = -math.ceil(self.max_speed / 2)


