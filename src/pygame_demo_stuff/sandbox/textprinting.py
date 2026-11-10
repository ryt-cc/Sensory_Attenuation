import sys
import pygame

pygame.init()
screen = pygame.display.set_caption("Text in Rect Example")
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

# Setup fonts and shapes
font = pygame.font.SysFont(None, 30)
my_box = pygame.Rect(150, 150, 300, 80)

item_texts = []
items = ["sword", "shield", "red potion", "blue potion"]
text_surf = font.render(items[-1], True, (255, 255, 255))
text_rect = text_surf.get_rect()

for index, item in enumerate(items):
    # Render text once outside the loop for better performance
    text_surf = font.render(item, True, (255, 255, 255))
    text_rect = text_surf.get_rect()
    # text_rect.top = my_box.top
    item_texts.append(text_surf)

# Center alignment


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((30, 30, 30))

    # Draw container rectangle
    # pygame.draw.rect(screen, (20, 120, 200), my_box)

    # Draw text container overlay
    for index, item_text in enumerate(item_texts):
        new_rect = text_rect.copy()
        new_rect.y += index * new_rect.height
        # screen.blit(item_text,text_rect)
        print(f"Drawing: {item_text}")
        screen.blit(item_text, new_rect)

    pygame.display.flip()
    clock.tick(60)
