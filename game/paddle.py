from game.point import Point
from game import constants

import arcade

class Paddle(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.PADDLE_IMAGE)

        self.center_x = int(constants.MAX_X / 2)
        self.center_y = int(constants.PADDLE_Y)
