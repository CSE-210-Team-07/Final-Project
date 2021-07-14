from game.point import Point
from game import constants

import arcade

class Brick(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(constants.BRICK_IMAGE)

        self.center_x = x
        self.center_y = y


