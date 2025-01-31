import pygame

import settings


class Terrain:
    def __init__(self):
        self.y_pos = 400

    def draw(self, screen):
        pygame.draw.line(screen, settings.WHITE, (0, self.y_pos), (600, self.y_pos), 3)

