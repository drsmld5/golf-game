import pygame
import settings
from ball import Ball


class Player:
    def __init__(self, pos_x, pos_y):
        self.ball = Ball(pos_x, pos_y)


