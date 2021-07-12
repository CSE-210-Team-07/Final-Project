import random
from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self):
        
        self.score = 0


    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        laser = cast["laser"][0] # there's only one
        paddle = cast["paddle"][0] # there's only one
        enemys = cast["enemy"]

        # gets current position and velocity values from laser
        x_Position = laser.get_position()
        x_Position = x_Position.get_x()
        y_Position = laser.get_position()
        y_Position = y_Position.get_y()
        y_Velocity = laser.get_velocity()
        y_Velocity = y_Velocity.get_y()
        x_Velocity = laser.get_velocity()
        x_Velocity = x_Velocity.get_x()
        Paddle_Position = paddle.get_position()

        #recognizes when laser hits bottom of the screen and bounces the laser
        #this is where the game needs to end
        if y_Position == 19:
            # velocity = Point(x_Velocity, -1)
            # laser.set_velocity(velocity)
            score = self.score
            score = str(score)
            laser.set_text("Game Over, Your score is: " + score)
            laser.set_position(Point(30,10))
            laser.set_velocity(Point(0,0))


        #bounces off ceiling
        if y_Position == 1:
            self.score += 1
            laser.set_position(Paddle_Position)


        #checks if laser is coliding with a enemy, changes y_velocity if it is
        for i in range(280):
            enemy = enemys[i]
            if enemy.get_position().equals(laser.get_position()):
                self.score += 1
                laser.set_position(Paddle_Position)
                enemy.set_text('')
                enemy.set_position(Point(10,1))
                
        
        # # checks if laser is coliding with paddle, changes y_velocity if it is
        # for i in range(6):
        #     pos = laser.get_position().add(Point(-i,0))
        #     if paddle.get_position().equals(pos):
        #         velocity = Point(-1, -1)
        #         laser.set_velocity(velocity)
        
        # for i in range(5):
        #     i += 6
        #     pos = laser.get_position().add(Point(-i,0))
        #     if paddle.get_position().equals(pos):
        #         velocity = Point(1, -1)
        #         laser.set_velocity(velocity)

        # # checks if laser is coliding with left and right borders, changes x_velocity if it is
        # if x_Position >= 79:
        #     velocity = Point(-1, y_Velocity)
        #     laser.set_velocity(velocity)
        # if x_Position <= 1:
        #     velocity = Point(1, y_Velocity)
        #     laser.set_velocity(velocity)

