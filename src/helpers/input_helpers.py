import pygame

from src.controllers.Actors.baseactor import CharacterAction, MoveDirection


def get_action_from_keypress() -> CharacterAction:
    held_keys = pygame.key.get_pressed()
    if held_keys[pygame.K_w] and held_keys[pygame.K_a]:
        return MoveDirection.NORTH_WEST
    elif held_keys[pygame.K_w] and held_keys[pygame.K_d]:
        return MoveDirection.NORTH_EAST
    elif held_keys[pygame.K_s] and held_keys[pygame.K_a]:
        return MoveDirection.SOUTH_EAST
    elif held_keys[pygame.K_s] and held_keys[pygame.K_d]:
        return MoveDirection.SOUTH_WEST

    elif held_keys[pygame.K_w]: #up
        return MoveDirection.NORTH
    elif held_keys[pygame.K_s]: #down
        return MoveDirection.SOUTH
    elif held_keys[pygame.K_a]: #left
        return MoveDirection.WEST
    elif held_keys[pygame.K_d]: #right
        return MoveDirection.EAST
    return MoveDirection.STOPPED
