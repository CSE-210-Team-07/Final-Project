from game import constants
from game.action import Action
from game.ball import Ball

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        direction = self._input_service.get_direction().scale(constants.PADDLE_MOVE_SCALE)
        shootTrueFalse = self._input_service.shoot()
        if shootTrueFalse:
            paddle = cast["paddle"][0] # there's only one in the cast
            paddle_x = paddle.center_x 
            ball = Ball(paddle_x)
            cast["balls"].append(ball)
        paddle = cast["paddle"][0] # there's only one in the cast
        paddle_x = paddle.center_x
        # print(paddle.center_x) 

        if paddle_x <= 0 and direction.get_x() == -10:
            paddle.center_x = constants.MAX_X
        elif paddle_x >= constants.MAX_X and direction.get_x() == 10:
            paddle.center_x = 0
        else:
            paddle.change_x = direction.get_x()
    

        # paddle.change_y = direction.get_y()
