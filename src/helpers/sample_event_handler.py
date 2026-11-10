import pygame
import time
name = "Qat"
def what_button_am_i_pressing():
    mouse_motion_debounce = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print(f"Start time : {time.time_ns()}") ## F strings you can insert vars into strings
                return time.time_ns()
            elif event.key == pygame.K_s:
                print("This is the go down button")
            elif event.key == pygame.K_i:
                print(f"I just open the inventory  you just cant see it")


