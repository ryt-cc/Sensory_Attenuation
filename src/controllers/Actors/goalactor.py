
import pygame

from src.controllers.Actors.ballactor import PlayerBall
from src.controllers.Actors.baseactor import BaseActor
from src.controllers.Actors.playerbaseactor import PlayerBase


class GoalActor(BaseActor):

    def __init__(self, goal_rect: pygame.Rect):
        super().__init__()
        self.rect = goal_rect

    def move(self):
        """Goals dont move"""
        pass

    def detect_player(self,players:list[PlayerBase]) -> PlayerBase | None:
        for _ in players:
            if self.rect.colliderect(_.collision_box):
                return _
        return None
