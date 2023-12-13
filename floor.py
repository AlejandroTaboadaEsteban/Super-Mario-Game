import constants
import pyxel


class Floor:
    """ This class stores all the information needed for the floor of the level"""
    def __init__(self, x: int, y: int):
        """ Its attributes are the x position and the y position of the floor block"""
        self.x = x
        self.y = y
        # The size (height and width) of every floor block will always be the same
        self.height = 16
        self.width = 16

    def show_floor(self):
        """ This method allows us to show the floor in the screen, by using the pyxel.blt function with
         the floor block x, y and sprite"""
        pyxel.blt(self.x, self.y, constants.FLOOR_SPRITE[0], constants.FLOOR_SPRITE[1], constants.FLOOR_SPRITE[2],
                  constants.FLOOR_SPRITE[3], constants.FLOOR_SPRITE[4])

    def move_floor(self, n):
        """ This method allows the floor to move while the background is moving, so that the level can progresses,
        and needs to be introduced with a parameter n that decides how much to move the floor"""
        self.x -= n