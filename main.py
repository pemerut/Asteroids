import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from shot import Shot

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")


main()

# Groups
#my_group = pygame.sprite.Group()
#Player.containers = (group_a, group_b)
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (shots, updatable, drawable)

player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
asteroidfield = AsteroidField()

clock = pygame.time.Clock()
dt = 0

loop_bool = True

while loop_bool:
    log_state()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop_bool = False

    screen.fill("black")
    updatable.update(dt)
    for asteroid in asteroids:
        for shot in shots:
            if shot.collides_with(asteroid):
                log_event("asteroid_shot")
                asteroid.kill()
                shot.kill()
        if asteroid.collides_with(player):
            log_event("player_hit")
            print("Game over!")
            sys.exit()
    for obj in drawable:
        obj.draw(screen)
    pygame.display.flip()
    dt = clock.tick(60) / 1000

    
    