from abc import ABC ,abstractmethod

import pygame
from pygame import Surface, Clock, Event

from src.controllers.games.constants import SCREEN_SIZE
from src.games.modals.resultsmodal import GameResults


class BaseGame(ABC):
    screen:Surface
    clock:Clock
    player:pygame.Rect
    goal:pygame.Rect

    def window_setup(self) -> None:
        self.screen = pygame.display.set_mode(SCREEN_SIZE, pygame.SCALED, vsync=1)

    def set_clock(self) -> None:
        self.clock = pygame.time.Clock()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    raise SystemExit
                self.keypress_event_handler(event)
            if event.type == pygame.KEYUP:
                self.keyrelease_event_handler(event)
            if event.type == pygame.MOUSEMOTION:
                self.mouse_motion_event_handler(event)
            if event.type == pygame.MOUSEBUTTONUP:
                self.mouse_press_event_handler(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_press_event_handler(event)

    @abstractmethod
    def keypress_event_handler(self,event:Event):
        """What happens when keys are pressed"""

    @abstractmethod
    def keyrelease_event_handler(self,event:Event):
        """What happens when keys are pressed"""

    @abstractmethod
    def mouse_motion_event_handler(self,event:Event):
        """What happens when keys are pressed"""

    @abstractmethod
    def mouse_press_event_handler(self,event:Event):
        """What happens when keys are pressed"""

    @abstractmethod
    def mouse_release_event_handler(self,event:Event):
        """What happens when keys are pressed"""


    @abstractmethod
    def start(self)-> None:
        '''Starts game'''
        pass

    @abstractmethod
    def collect_results(self) -> GameResults:
        '''Returns results as GameResults Object'''



