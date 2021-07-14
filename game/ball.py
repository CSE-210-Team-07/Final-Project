from game.paddle import Paddle
from game.point import Point
from game import constants

from random import randint

import arcade

class Ball(arcade.Sprite):
    def __init__(self):

        super().__init__(constants.BALL_IMAGE)

        self.center_x = constants.MAX_X / 2
        self.center_y = constants.PADDLE_Y

        self.change_x = constants.BALL_SPEED
        self.change_y = constants.BALL_SPEED

    def bounce_horizontal(self):
        self.change_y *= -1

    def bounce_vertical(self):
        self.change_x *= 0

