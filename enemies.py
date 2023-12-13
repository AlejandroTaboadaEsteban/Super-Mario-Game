import constants
import pyxel
from mario import Mario


class Enemies:
    """ This class stores all the information needed for the enemies"""
    def __init__(self, type: int, x: int, mario: Mario):
        """ Its attributes are the type of the enemy, given as an integer (1 is koopa tropa and 2,3 and 4 are goomba),
         which allows to randomly select the type of the enemy, the x position of the enemy and a Mario to interact
         with"""
        self.x = x
        # The initial direction for all the enemies will be left
        self.dir = "left"
        self.type = type
        # Since the enemies will only move on the ground, their y position wont change
        # We set it depending on their type, because the koopa troopas are taller than the goombas
        # That's why for koopa troopa it will be 200, and for goomba 208
        if self.type == 1:
            self.y = 200
        else:
            self.y = 208
        self.goomba_sprite = constants.GOOMBA_SPRITE
        self.koopatroopa_sprite = constants.KOOPA_SPRITE
        self.mario = mario
        # All the enemies will have a width of 16
        self.width = 16

    def move_enemies(self):
        """ This method defines the movement of all the enemies, with different speeds depending on the direction
        of the enemy, if Mario is sprinting or if the background is moving"""
        if self.mario.x >= 120 and pyxel.btn(pyxel.KEY_RIGHT) and self.dir == "left":
            if pyxel.btn(pyxel.KEY_LEFT_SHIFT):
                # If Mario is sprinting, the enemy is going left and the background is moving
                self.x -= 9
            else:
                # If Mario isn't sprinting, the enemy is going left and the background is moving
                self.x -= 5
        elif self.mario.x >= 120 and pyxel.btn(pyxel.KEY_RIGHT) and self.dir == "right":
            if pyxel.btn(pyxel.KEY_LEFT_SHIFT):
                # If Mario is sprinting, the enemy is going right and the background is moving
                self.x -= 7
            else:
                # If Mario isn't sprinting, the enemy is going right and the background is moving
                self.x -= 3
        elif self.dir == "right":
            # If the enemy is going right and the background isn't moving
            self.x += 1
        else:
            # If the enemy is going left and the background isn't moving
            self.x -= 1

    def show_enemies(self):
        """ This method shows the enemies in the screen, and gives them an aspect depending on their type,
        so that goombas are different to koopa troopas"""
        if self.type == 1:
            # In the case of koopa troopa, the appearance changes depending on its direction
            if self.dir == "left":
                pyxel.blt(self.x, self.y, self.koopatroopa_sprite[0],
                          self.koopatroopa_sprite[1], self.koopatroopa_sprite[2],
                          -self.koopatroopa_sprite[3], self.koopatroopa_sprite[4], colkey=12)
            elif self.dir == "right":
                pyxel.blt(self.x, self.y, self.koopatroopa_sprite[0],
                          self.koopatroopa_sprite[1], self.koopatroopa_sprite[2],
                          self.koopatroopa_sprite[3], self.koopatroopa_sprite[4], colkey=12)
        else:
            # In the case of goomba, the direction doesn't affect the appearance
            pyxel.blt(self.x, self.y, self.goomba_sprite[0],
                      self.goomba_sprite[1], self.goomba_sprite[2],
                      self.goomba_sprite[3], self.goomba_sprite[4], colkey=12)