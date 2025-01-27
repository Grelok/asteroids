from random import uniform

import pygame.draw

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color('white'), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        dev = uniform(20, 50)
        ndir1 = self.velocity.rotate(-dev)
        ndir2 = self.velocity.rotate(dev)
        nsize = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, nsize)
        a1.velocity = ndir1 * 1.2
        a2 = Asteroid(self.position.x, self.position.y, nsize)
        a2.velocity = ndir2 * 1.2

