import os

MAX_X = 800
MAX_Y = 600
NUM_BALLS = 1

BALL_SPEED = 3
BALL_Y = MAX_Y / 2
BALL_X = MAX_Y / 2

PADDLE_Y = 50

PADDLE_MOVE_SCALE = 10

BRICK_WIDTH = 25
BRICK_HEIGHT = 15
BRICK_SPACE = 10

BALLS_CAN_DIE = True
PATH = os.path.dirname(os.path.abspath(__file__))
BALL_IMAGE = os.path.join(PATH,'..','images', 'ball-0.png')
PADDLE_IMAGE = os.path.join(PATH,'..','images', 'paddle-0.png')
BRICK_IMAGE = os.path.join(PATH,'..','images', 'brick-0.png')

