import constants
import time
import pyxel


class Score:
    """ This class stores all the information needed for the score of the game"""
    def __init__(self):
        # This variable stores the points that Mario obtains
        self.score = 0
        # This one the coins that Mario obtains
        self.coins = 0
        # This one the lives remaining
        self.lives = constants.LIVES
        # These three are used to show the time remaining
        # The first one is the maximum time, and the second one works like a clock that starts counting
        self.time_final = constants.TIME
        self.time_initial = time.time()
        # This one is the difference between the other times, so it is the time remaining
        self.time_remaining = None
        # These are the sprites we are going to use
        self.spritecoins = constants.SCORE_LIVES_SPRITE
        self.spritelives = constants.SCORE_COINS_SPRITE
        # And this variables is used to know when Mario wins
        self.end = False

    def show_screen(self):
        """ This method shows in the screen a score with the lives, points, coins, time remaining and some text of the
         level"""
        x_initial = 32
        row1 = 20
        row2 = 32
        # This shows the score, the number 7 is to make the numbers white
        pyxel.text(x_initial, row2, str(self.score).zfill(6), 7)
        # This shows the name Mario
        pyxel.text(x_initial, row1, "MARIO", 7)
        # This shows the world text
        pyxel.text(x_initial + 45, row2, "1/1", 7)
        pyxel.text(x_initial + 45, row1, "WORLD", 7)
        # This shows the amount of coins obtained
        pyxel.text(x_initial * 4, row2, "x" + str(self.coins).zfill(2), 7)
        # This shows the lives remaining
        pyxel.text(x_initial * 5, row2, "x" + str(self.lives).zfill(2), 7)
        # This shows the time remaining
        self.time_remaining = self.time_final - int(time.time() - self.time_initial)
        pyxel.text(x_initial * 6, row2, str(self.time_remaining).zfill(3), 7)
        # This shows the word time
        pyxel.text(x_initial * 6, row1, "TIME", 7)
        # And this two pyxel functions show in the screen the symbol of the coins and the lives
        pyxel.blt(110, 26, self.spritecoins[0], self.spritecoins[1],
                  self.spritecoins[2], self.spritecoins[3], self.spritecoins[4], colkey=12)
        pyxel.blt(143, 26, self.spritelives[0], self.spritelives[1],
                  self.spritelives[2], self.spritelives[3], self.spritelives[4], colkey=12)
        # These commands turn the lives into 0 when the time finishes
        if self.time_remaining < 1:
            self.lives = 0

    def lose_game(self):
        """ This method is used when Mario loses, to show a game over screen"""
        # It activates when Mario has 0 lives
        if self.lives < 1:
            # And it changes to the game over screen
            pyxel.bltm(0, 0, 0, 0, 0, 64, 64)

    def win_game(self):
        """ This method is used when Mario wins, when it passed through the flag at the end of the level"""
        if self.end:
            x_initial = 32
            row1 = 20
            row2 = 32
            # It changes to the victory screen
            pyxel.bltm(0, 0, 0, 32, 0, 64, 64)
            # It also adds some information of the passed level
            # This shows the word points
            pyxel.text(x_initial, row1, "POINTS", 7)
            # This shows the score
            pyxel.text(x_initial, row2, str(self.score).zfill(6), 7)
            # This shows the coins obtained and the coin symbol
            pyxel.text(x_initial * 4, row2, "x" + str(self.coins).zfill(2), 7)
            pyxel.blt(110, 26, self.spritecoins[0], self.spritecoins[1],
                      self.spritecoins[2], self.spritecoins[3], self.spritecoins[4], colkey=12)
            # And this shows the lives remaining and the life symbol
            pyxel.text(x_initial * 6 + 10, row2, "x" + str(self.lives).zfill(2), 7)
            pyxel.blt(185, 26, self.spritelives[0], self.spritelives[1],
                      self.spritelives[2], self.spritelives[3], self.spritelives[4], colkey=12)