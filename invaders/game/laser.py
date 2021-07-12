from game.actor import Actor
from game.point import Point

class Laser:
    """Represents distance from an origin (0, 0).

    Stereotype:
        Information Holder

    Attributes:
        _x (integer): The horizontal distance.
        _y (Point): The vertical distance.
    """
    
    def __init__(self, cast):
        paddle = cast["paddle"][0]
        
        paddle_Position = paddle.get_position()
        x_Position = x_Position.get_x()

        
        position = paddle_Position
        velocity = Point(-1, 0)
        laser = Actor()
        laser.set_text("|")
        laser.set_position(position)
        laser.set_velocity(velocity)
    
    