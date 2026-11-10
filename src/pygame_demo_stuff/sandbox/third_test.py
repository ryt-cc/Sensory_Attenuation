import csv
import time
from random import random

import pygame

from src.pygame_demo_stuff.controllers.Characters.playermodal import Player
from src.helpers.sample_event_handler import what_button_am_i_pressing

pygame.init()

screen = pygame.display.set_mode((1280,720),pygame.SCALED,vsync=1)

clock = pygame.time.Clock()

square_ball_visible = Player("Cool elf girl", (20, 40))
square_ball_hitbox = Player("Sneaky",(5,5))

center_of_screen = (round(screen.width/2),round(screen.height/2))
square_ball_visible.jump_to(center_of_screen)
square_ball_hitbox.jump_to(center_of_screen)

mouse_on_ball = False
goal = Player("the Hole", (200, 400))
goal.jump_to((500,500))
start_time = 0
end_time = 0
game_won  = False
trials = 0
while True :
    # Process Characters inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            pass
        if event.type == pygame.MOUSEBUTTONDOWN:
            ball_location = square_ball_visible.rect.center
            where_is_my_mouse = pygame.mouse.get_pos()
            if square_ball_visible.rect.collidepoint(where_is_my_mouse):
                print("This is way less gross dummy")
                mouse_on_ball = True
                start_time = time.time_ns()

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_on_ball = False


        if event.type == pygame.MOUSEMOTION:
            where_is_my_mouse = pygame.mouse.get_pos()
            if mouse_on_ball:
                square_ball_visible.rect.center = where_is_my_mouse
                square_ball_hitbox.rect.center = square_ball_visible.rect.center
            if goal.rect.colliderect(square_ball_hitbox.rect) and game_won == False:

                end_time = time.time_ns()
                time_to_complete = (end_time-start_time)  / 1e9
                print(f"You are the winner with a time of {time_to_complete}")
                end_time = 0
                start_time = 0
                game_won = True

    if game_won == True and trials < 3:
        square_ball_visible.jump_to((100, 100))
        pygame.mouse.set_pos(100,100)
        game_won = False
        trials += 1
            # print(f"My mouse is located at {where_is_my_mouse}")

            #


    # Do logical updates here.
    # ...
    screen.fill("black")  # Fill the display with a solid color
    pygame.draw.rect(screen, "blue", square_ball_visible.rect)
    pygame.draw.rect(screen, "red", goal.rect)

    # Render the graphics here,
    # ...
    pygame.display.flip()  # Refresh on-screen display
    clock.tick(240)         # wait until next frame (at 60 FPS)

