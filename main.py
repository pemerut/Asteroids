import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")


main()

loop_bool = True

while loop_bool:
    log_state()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop_bool = False

    screen.fill("black")
    pygame.display.flip()