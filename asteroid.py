import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        chunk1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        random_angle = random.uniform(20,50)
        chunk1.velocity = self.velocity.rotate(random_angle) * 1.2
        chunk2 = Asteroid(self.position.x, self.position.y , self.radius - ASTEROID_MIN_RADIUS)
        chunk2.velocity = self.velocity.rotate(-random_angle) * 1.2
