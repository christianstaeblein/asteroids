import pygame
import circleshape
import constants
from logger import log_event
import random
import asteroid

class Asteroid(circleshape.CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen,"white",self.position,self.radius,constants.LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            velocity1 = self.velocity.rotate(angle)
            velocity2 = self.velocity.rotate(-angle)

            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

            log_event("asteroid_split")

            asteroid1 = Asteroid(self.position.x,self.position.y,new_radius)
            asteroid1.velocity = asteroid1.velocity.rotate(angle)
            asteroid1.velocity = velocity1 * 1.2

            asteroid2 = Asteroid(self.position.x,self.position.y,new_radius)
            asteroid2.velocity = asteroid2.velocity.rotate(angle*-1)
            asteroid2.velocity = velocity2 * 1.2
