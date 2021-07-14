import random
import arcade



SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_ENEMY = 0.2
SPRITE_SCALING_LASER = 0.8
ENEMY_COUNT = 40
ENEMY_SPEED = 2
ENEMY_DOWNWARD_DROP = 20
PLAYER_MOVEMENT_SPEED = 3

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Space Invadors"

BULLET_SPEED = 10

class MyGame(arcade.Window):
    
    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        self.player_list = None
        self.enemy_list = None
        self.bullet_list = None

        self.player_sprite = None
        self.score = 0
        self.enemy_change_x = -ENEMY_SPEED

        arcade.set_background_color(arcade.color.SPACE_CADET)
    
    def setup(self):

        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = (SCREEN_WIDTH/2)
        self.player_sprite.center_y = (SCREEN_HEIGHT/4)
        self.player_list.append(self.player_sprite)

        for i in range(ENEMY_COUNT):
            enemy = arcade.Sprite(":resources:images/items/coinGold.png", SPRITE_SCALING_ENEMY)
            i += 1
            if (i >= 0 and i <= 11):
                enemy.center_x = SCREEN_WIDTH - (i * 75)
                enemy.center_y = SCREEN_HEIGHT - 50
            if (i >= 11 and i <= 21):
                enemy.center_x = SCREEN_WIDTH - ((i-10) * 75)
                enemy.center_y = SCREEN_HEIGHT - 75
            if (i >= 21 and i <= 31):
                enemy.center_x = SCREEN_WIDTH - ((i-20) * 75)
                enemy.center_y = SCREEN_HEIGHT - 100
            if (i >= 31 and i <= 41):
                enemy.center_x = SCREEN_WIDTH - ((i-30) * 75)
                enemy.center_y = SCREEN_HEIGHT - 125
            self.enemy_list.append(enemy)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.enemy_list)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.enemy_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()

        # Render the text
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.SPACE:
            # arcade.play_sound(self.gun_sound)
            # Create a bullet
            bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", SPRITE_SCALING_LASER)

            # The image points to the right, and we want it to point up. So
            # rotate it.
            bullet.angle = 90

            # Give the bullet a speed
            bullet.change_y = BULLET_SPEED

            # Position the bullet
            bullet.center_x = self.player_sprite.center_x
            bullet.bottom = self.player_sprite.top

            # Add the bullet to the appropriate lists
            self.bullet_list.append(bullet)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """
        # Call update on bullet sprites
        self.bullet_list.update()
        

        self.physics_engine.update()

        move_down = False
        for enemy in self.enemy_list:
            if (enemy.center_x > SCREEN_WIDTH):
                self.enemy_change_x = -ENEMY_SPEED
                move_down = True
            elif (enemy.center_x < 0):
                self.enemy_change_x = ENEMY_SPEED
                move_down = True

        for enemy in self.enemy_list:
            enemy.center_x += self.enemy_change_x

        if (move_down == True):
            for enemy in self.enemy_list:
                enemy.center_y -= ENEMY_DOWNWARD_DROP

        
        


        # Loop through each bullet
        for bullet in self.bullet_list:

            # Check this bullet to see if it hit a enemy
            hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)

            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()

            # For every enemy we hit, add to the score and remove the enemy
            for enemy in hit_list:
                enemy.remove_from_sprite_lists()
                self.score += 1


            # If the bullet flies off-screen, remove it.
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()

def main():
    window = MyGame()
    window.setup()
    arcade.run()

main()