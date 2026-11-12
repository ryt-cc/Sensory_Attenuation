import pygame

from src.controllers.Actors.ballactor import PlayerBall
from src.controllers.Actors.playeractor import Player

pygame.init()

screen = pygame.display.set_mode((1280,720),pygame.DOUBLEBUF,vsync=1)

clock = pygame.time.Clock()

square_ball_visible = PlayerBall()
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
    # Process Actors inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            pass
        if event.type == pygame.MOUSEBUTTONDOWN:
         pass

    if game_won == True and trials < 3:
        square_ball_visible.jump_to((100, 100))
        pygame.mouse.set_pos(100,100)
        game_won = False
        trials += 1

    goal.move()
    square_ball_visible.move()


    screen.fill("black")  # Fill the display with a solid color
    pygame.draw.rect(screen, "red", goal.rect)
    pygame.draw.circle(screen, "blue", square_ball_visible.rect.center,30)


    # Render the graphics here,
    # ...
    pygame.display.flip()  # Refresh on-screen display
    clock.tick(240)         # wait until next frame (at 60 FPS)

