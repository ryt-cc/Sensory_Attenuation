import pygame

from pygame.draw import rect

pygame.init()
screen = pygame.display.set_mode((800,600),pygame.SCALED,vsync=1)
clock = pygame.time.Clock()



player = pygame.Rect(screen.width/2,screen.height/2,80,160)

max_speed = 10
accel_speed = 1
drag = .5
player_x_velocity = 0
player_y_velocity = 0

screen.fill("purple")  # Fill the display with a solid color

while True:
    if player_y_velocity > 0:
        player_y_velocity -= drag
    elif player_y_velocity < 0:
        player_y_velocity += drag
    if player_x_velocity > 0:
        player_x_velocity -= drag
    elif player_x_velocity < 0:
        player_x_velocity += drag

    current_play_rect = player.copy()
    # Process Characters inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                raise SystemExit
    held_keys = pygame.key.get_pressed()
    if held_keys[pygame.K_w]: #up
        player_y_velocity -= accel_speed
    if held_keys[pygame.K_s]: #down
        player_y_velocity += accel_speed
    if held_keys[pygame.K_a]: #left
        player_x_velocity -= accel_speed
    if held_keys[pygame.K_d]: #right
        player_x_velocity += accel_speed


    if player_x_velocity > max_speed:
        player_x_velocity = max_speed
    if player_y_velocity > max_speed:
        player_y_velocity = max_speed

    player.move_ip(player_x_velocity,player_y_velocity)

    pygame.draw.rect(screen,"purple",current_play_rect)
    pygame.draw.rect(screen, "blue", player)

    # Render the graphics here.
    # ...

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(120)         # wait until next frame (at 60 FPS)