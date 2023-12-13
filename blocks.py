import pyxel
import constants


class Blocks:
    """ This class stores all the information needed for the blocks of the level, that will be used for the collisions
     of Mario"""
    def __init__(self, x: int, y: int, type: str):
        """ Its attributes are the x and y position of the block, and its type"""
        self.x = x
        self.y = y
        self.type = type
        # depending on the type of the block we set its width and height
        if self.type == "normal" or self.type == "coin" or self.type == "mushroom" or self.type == "unbreakable" or \
                self.type == "broken" or self.type == "flag down" or self.type == "flag" or self.type == "flag up" or \
                self.type == "mushroom object":
            self.height = 16
            self.width = 16
        elif self.type == "pipe up" or self.type == "pipe down":
            self.height = 16
            self.width = 32

    def show_blocks(self):
        """ This method allows us to show the blocks in the screen, and the sprites used to represent each block
        depend on its type"""
        if self.type == "normal":
            pyxel.blt(self.x, self.y, constants.NORMAL_BLOCK_SPRITE[0], constants.NORMAL_BLOCK_SPRITE[1],
                      constants.NORMAL_BLOCK_SPRITE[2], constants.NORMAL_BLOCK_SPRITE[3],
                      constants.NORMAL_BLOCK_SPRITE[4])
        elif self.type == "coin":
            pyxel.blt(self.x, self.y, constants.COIN_BLOCK_SPRITE[0], constants.COIN_BLOCK_SPRITE[1],
                      constants.COIN_BLOCK_SPRITE[2], constants.COIN_BLOCK_SPRITE[3],
                      constants.COIN_BLOCK_SPRITE[4])
        elif self.type == "mushroom":
            pyxel.blt(self.x, self.y, constants.MUSHROOM_BLOCK_SPRITE[0], constants.MUSHROOM_BLOCK_SPRITE[1],
                      constants.MUSHROOM_BLOCK_SPRITE[2], constants.MUSHROOM_BLOCK_SPRITE[3],
                      constants.MUSHROOM_BLOCK_SPRITE[4])
        elif self.type == "unbreakable":
            pyxel.blt(self.x, self.y, constants.UNBREAKABLE_BLOCK_SPRITE[0], constants.UNBREAKABLE_BLOCK_SPRITE[1],
                      constants.UNBREAKABLE_BLOCK_SPRITE[2], constants.UNBREAKABLE_BLOCK_SPRITE[3],
                      constants.UNBREAKABLE_BLOCK_SPRITE[4])
        elif self.type == "pipe up":
            pyxel.blt(self.x, self.y, constants.PIPE_UP_SPRITE[0], constants.PIPE_UP_SPRITE[1],
                      constants.PIPE_UP_SPRITE[2], constants.PIPE_UP_SPRITE[3],
                      constants.PIPE_UP_SPRITE[4])
        elif self.type == "pipe down":
            pyxel.blt(self.x, self.y, constants.PIPE_DOWN_SPRITE[0], constants.PIPE_DOWN_SPRITE[1],
                      constants.PIPE_DOWN_SPRITE[2], constants.PIPE_DOWN_SPRITE[3],
                      constants.PIPE_DOWN_SPRITE[4])
        elif self.type == "broken":
            pyxel.blt(self.x, self.y, constants.BROKEN_BLOCK_SPRITE[0], constants.BROKEN_BLOCK_SPRITE[1],
                      constants.BROKEN_BLOCK_SPRITE[2], constants.BROKEN_BLOCK_SPRITE[3],
                      constants.BROKEN_BLOCK_SPRITE[4])
        elif self.type == "flag down":
            pyxel.blt(self.x, self.y, constants.FLAG_DOWN_SPRITE[0], constants.FLAG_DOWN_SPRITE[1],
                      constants.FLAG_DOWN_SPRITE[2], constants.FLAG_DOWN_SPRITE[3],
                      constants.FLAG_DOWN_SPRITE[4])
        elif self.type == "flag":
            pyxel.blt(self.x, self.y, constants.FLAG_SPRITE[0], constants.FLAG_SPRITE[1],
                      constants.FLAG_SPRITE[2], constants.FLAG_SPRITE[3],
                      constants.FLAG_SPRITE[4])
        elif self.type == "flag up":
            pyxel.blt(self.x, self.y, constants.FLAG_UP_SPRITE[0], constants.FLAG_UP_SPRITE[1],
                      constants.FLAG_UP_SPRITE[2], constants.FLAG_UP_SPRITE[3],
                      constants.FLAG_UP_SPRITE[4])
        elif self.type == "mushroom object":
            pyxel.blt(self.x, self.y, constants.MUSHROOM_SPRITE[0], constants.MUSHROOM_SPRITE[1],
                      constants.MUSHROOM_SPRITE[2], constants.MUSHROOM_SPRITE[3],
                      constants.MUSHROOM_SPRITE[4])

    def move_blocks(self, n):
        """ This method moves all the blocks by decreasing their x position, and has a parameter to decide how much
        should the blocks me moved"""
        self.x -= n