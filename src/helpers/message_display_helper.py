import pygame
from pygame import Surface


def display_message(message:str) -> tuple[Surface,pygame.Rect]:
    pygame.init()
    font = pygame.font.SysFont(None, 48)
    text_surface = font.render(message, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(300, 200))
    return text_surface,text_rect