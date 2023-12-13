import constants
import pyxel


class Mario:
    """ This class stores all the information needed for Mario"""
    def __init__(self, x: int, y: int, dir: bool):
        """ Its attributes are the x position of Mario, the y position of Mario and Mario's direction, expressed as
        a boolean, where True is right and False is left"""
        self.x = x
        self.y = y
        self.relative_y = 0
        self.direction = dir
        # Here is the initial sprite for Mario
        self.sprite = constants.MARIO_SPRITE
        # We also assume that Mario will always have three lives in the beginning
        self.lives = 3
        # These are some variables used for the jump of Mario
        self.jumping = False
        self.speed = constants.SPEED
        self.gravity = constants.GRAVITY
        self.going_up = False
        # This variable stores if Mario is big (if it has taken a mushroom)
        self.big = False
        # And these are the inial height and width of Mario, that will be needed for many interactions
        self.height = constants.MARIO_SPRITE[4]
        self.width = constants.MARIO_SPRITE[3]

    def move(self, direction: str, size: int, sprint=False):
        """ This method is used to move mario, and it has as parameters the direction of the movement,
        the size, and if it is a sprint (which would increase the speed of the movement). The sprint will be False as
         default,but it will be possible to change it"""
        # Depending on Mario's direction and on if Mario is big it changes Mario's sprite
        if self.direction:
            if not self.big:
                # If Mario is going right and is not big
                self.sprite = constants.MARIO_SPRITE
            elif self.big:
                # If mario is going right and is big
                self.sprite = constants.MARIO_BIG_SPRITE
        elif not self.direction:
            if not self.big:
                # If Mario is going left and isn't big
                self.sprite = (constants.MARIO_SPRITE[0], constants.MARIO_SPRITE[1],
                               constants.MARIO_SPRITE[2], -constants.MARIO_SPRITE[3],
                               constants.MARIO_SPRITE[4])
            elif self.big:
                # If Mario is going left and is big
                self.sprite = (constants.MARIO_BIG_SPRITE[0], constants.MARIO_BIG_SPRITE[1],
                               constants.MARIO_BIG_SPRITE[2], -constants.MARIO_BIG_SPRITE[3],
                               constants.MARIO_BIG_SPRITE[4])
                # This is the size of the movement
        mario_x_size = self.sprite[3]
        if direction.lower() == 'right' and self.x < size - mario_x_size:
            # If the movement is to the right, the direction will turn to right,and Mario's x will increase
            self.direction = True
            if sprint:
                # If it is also sprinting the movement would be the following
                self.x += 4
            else:
                # If it is not sprinting the movement would be like this
                self.x += 2
        elif direction.lower() == 'left' and self.x > 0:
            # If the movement is to the left it will also change the direction, and Mario's x will decrease
            self.direction = False
            if sprint:
                # If Mario is sprinting it will decrease faster
                self.x -= 4
            else:
                # And if Mario is not sprinting it will decrease slower
                self.x -= 2

    def jump(self):
        """ This method is used to make Mario jump"""
        # When the variable relative.y is 0 mario will be able to jump
        if self.relative_y == 0:
            # And it will jump if space bar or up arrow is pressed
            if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_UP):
                # If these keys pressed the jumping variable will turn True
                self.jumping = True
            else:
                # If they aren't pressed, jumping will be False, and the speed will return to its initial value
                self.jumping = False
                self.speed = constants.SPEED
        if self.jumping:
            # The speed will decrease due to the gravity
            self.speed -= self.gravity
            if self.speed > 0:
                # If the speed is larger than 0 going up will be True
                self.going_up = True
            elif self.speed <= 0:
                # If it is smaller or equal to 0 going up will turn False
                self.going_up = False
            # Mario's y will decrease depending on its speed
            self.y -= self.speed
            # And the relative_y will increase so that it's different to 0 and Mario can't double jump
            self.relative_y += 1
        # Mario's y will be adjusted not to be below the floor
        if self.y + self.height > 224:
            self.y = 224 - self.height
        if self.y == 224 - self.height:
            # If Mario's on the floor relative_y will turn 0 again to be able to jump
            self.relative_y = 0