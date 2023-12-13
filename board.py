
from mario import Mario
import pyxel
from score import Score
from collisions import Collisions


class Board:
    """ This class contains all the information needed to represent the
    board, it will import all the other classes to make the game work"""
    def __init__(self, w: int, h: int):
        """ Its attributes are the width and the height of the board"""
        self.width = w
        self.height = h
        # It creates a score and a Mario to interact with them
        self.score = Score()
        self.mario = Mario(30, 208, True)
        # It also creates the move_map variables that will be used to move the background
        self.move_map = 0
        # And it also creates a collisions variable
        self.collisions = Collisions(self.mario, self.score)
        # And from this last variable it imports a blocks, floor and enemies variable
        self.blocks = self.collisions.blocks
        self.floor = self.collisions.floor
        self.enemies = self.collisions.enemies

    def update(self):
        """ This method updates the game every second, it has a lot of methods and functions in it that have to be
        constantly executing"""
        # It allows you to exit the game by pressing q
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        # If the game has not ended it allows you to move, making the background, blocks and floor move too
        if not self.score.end:
            if pyxel.btn(pyxel.KEY_RIGHT):
                # If you press right key this activates
                if self.mario.x < self.width/2 - 8:
                    # If Mario is at the left part of the screen he will be who moves, and shift will make him sprint
                    if pyxel.btn(pyxel.KEY_LEFT_SHIFT):
                        self.mario.move('right', self.width, True)
                    else:
                        self.mario.move('right', self.width)
                else:
                    # If mario is at the half of the screen the screen and all the objects will move instead of Mario
                    # Shift will also influence the movement, because it will make blocks move faster
                    if pyxel.btn(pyxel.KEY_LEFT_SHIFT):
                        self.move_map += 1
                        for i in range(len(self.blocks)):
                            self.blocks[i].move_blocks(8)
                        for i in range(len(self.floor)):
                            self.floor[i].move_floor(8)
                    else:
                        self.move_map += 0.5
                        for i in range(len(self.blocks)):
                            self.blocks[i].move_blocks(4)
                        for i in range(len(self.floor)):
                            self.floor[i].move_floor(4)
            elif pyxel.btn(pyxel.KEY_LEFT):
                # If left key is moved only Mario will move left, by decreasing its x
                # Its x will decrease higher if Mario is sprinting
                if pyxel.btn(pyxel.KEY_LEFT_SHIFT):
                    self.mario.move('left', self.width, True)
                else:
                    self.mario.move('left', self.width)
            # Update also has in Mario's jump, Mario's fall, Mario's collisions, and Mario's collisions
            self.mario.jump()
            self.collisions.interactions()
            self.collisions.fall()
            # And it will also have the movement of the enemies and their collisions
            for i in range(len(self.enemies)):
                self.enemies[i].move_enemies()
            self.collisions.enemies_collision()
            # Finally, it also has the interactions of the enemies with Mario, when they die or Mario loses a life
            self.collisions.die_mario()
            self.collisions.kill_enemies()

    def draw(self):
        """ This method draws in the screen all the things that should be drawn, so there are a lot of methods in it
        too"""
        # It executes the background function, that makes the background move
        self.background()
        # And it also draws all the blocks, enemies and floor, one by one in each list with its corresponding function
        for i in range(len(self.blocks)):
            self.blocks[i].show_blocks()
        for i in range(len(self.floor)):
            self.floor[i].show_floor()
        for i in range(len(self.enemies)):
            self.enemies[i].show_enemies()
        # It draws Mario taking the values from the mario object
        pyxel.blt(self.mario.x, self.mario.y, self.mario.sprite[0],
                  self.mario.sprite[1], self.mario.sprite[2], self.mario.sprite[3],
                  self.mario.sprite[4], colkey=12)
        # It also shows the score
        self.score.show_screen()
        # And has the wining and losing functions in case that needed
        self.score.lose_game()
        self.score.win_game()

    def background(self):
        """ This method moves the background depending on a variable that is defined in the class and that changes when
        Mario is moving"""
        pyxel.bltm(0, 0, 0, self.move_map, 66, 64, 64)