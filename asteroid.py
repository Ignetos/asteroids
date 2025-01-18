import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        if self.position.x < (0 - self.radius):
            self.position.x = SCREEN_WIDTH
        if self.position.x > (SCREEN_WIDTH + self.radius):
            self.position.x = 0
        if self.position.y < (0 - self.radius):
            self.position.y = SCREEN_HEIGHT
        if self.position.y > (SCREEN_HEIGHT + self.radius):
            self.position.y = 0

        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(angle)
        velocity2 = self.velocity.rotate(-angle)
        radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, radius)
        asteroid1.velocity = velocity1 * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, radius)
        asteroid2.velocity = velocity2 * 1.2