import pygame

from src.controllers.Actors.baseactor import BaseActor, MoveDirection
from src.helpers.input_helpers import get_action_from_keypress


class Player(BaseActor):

    def move(self):
        action = get_action_from_keypress()
        if isinstance(action, MoveDirection):
            self.movement_direction = action
            self.apply_acceleration()
            self.apply_speed_limit()
            self.apply_drag()
            self.rect.move_ip(self.x_speed, self.y_speed)





