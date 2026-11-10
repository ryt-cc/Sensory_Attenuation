import time

import pygame

from src.helpers.sample_event_handler import what_button_am_i_pressing

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()

mouse_motion_debounce = False
start_time = None
end_time = None
while True:
    # Process Characters inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print(f"Start time : {time.time_ns()}")  ## F strings you can insert vars into strings
                start_time = time.time_ns()
            elif event.key == pygame.K_s:
                print("You stopped the time, winner")
                end_time = time.time_ns()
            elif event.key == pygame.K_i:
                print(f"I just open the inventory  you just cant see it")

    # Do logical updates here.
    # ...
    if start_time and end_time:
        final_time = end_time - start_time
        print(f"You final time it {final_time}")
        pygame.quit()
        raise SystemExit
    screen.fill("black")  # Fill the display with a solid color

    # Render the graphics here.
    # ...

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)