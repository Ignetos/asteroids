import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

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