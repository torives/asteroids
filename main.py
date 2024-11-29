import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(pygame.Color("black"))
        for sprite in updatable:
            sprite.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.did_collide(shot):
                    shot.kill()
                    asteroid.kill()
            if asteroid.did_collide(player):
                print("Game over!")
                exit()
            
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        
        # limit the framerate to 60 FPS
        dt = clock.tick(60)/1000
    

if __name__ == "__main__":
    main()