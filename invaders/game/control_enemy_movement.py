import random
from typing import cast
from game import constants
from game.action import Action
from game.point import Point

class ControlEnemyMovement(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self):
        
        self.timer = 0
 


    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        laser = cast["laser"][0] # there's only one
        paddle = cast["paddle"][0] # there's only one
        enemys = cast["enemy"]

        # gets current position and velocity values from enemy
        
        Paddle_Position = paddle.get_position()


        #checks if laser is coliding with a enemy, changes y_velocity if it is
        for i in range(280):
            enemy = enemys[i]
            x_Position = enemy.get_position()
            x_Position = x_Position.get_x()
            y_Position = enemy.get_position()
            y_Position = y_Position.get_y()
            y_Velocity = enemy.get_velocity()
            y_Velocity = y_Velocity.get_y()
            x_Velocity = enemy.get_velocity()
            x_Velocity = x_Velocity.get_x()
            if (x_Position > 78 and x_Velocity == 1) or (x_Position < 2 and x_Velocity == -1):
                self.timer += 1
                self.change_direction(cast)
                break

    
    def change_direction(self, cast):
        enemys = cast['enemy']
        for i in range(280):
            enemy = enemys[i]
            x_Position = enemy.get_position()
            x_Position = x_Position.get_x()
            y_Position = enemy.get_position()
            y_Position = y_Position.get_y()
            y_Velocity = enemy.get_velocity()
            y_Velocity = y_Velocity.get_y()
            x_Velocity = enemy.get_velocity()
            x_Velocity = x_Velocity.get_x()
            new_velocity = Point(x_Velocity * -1, y_Velocity)
            enemy.set_velocity(new_velocity)
            if self.timer > 9:
                new_position = Point(x_Position, y_Position + 1)
                enemy.set_position(new_position)
        if self.timer > 9:
            self.timer = 0    


                
        
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

