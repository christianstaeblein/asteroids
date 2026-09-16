import pygame
import constants
import player
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0

    p = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return



        screen.fill(pygame.Color("black"))
        p.update(dt)
        p.draw(screen)

        pygame.display.flip()



        dt= clock.tick(60)/1000


if __name__ == "__main__":
    main()
