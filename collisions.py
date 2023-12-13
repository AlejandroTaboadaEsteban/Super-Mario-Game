import random
import constants
from floor import Floor
from mario import Mario
from blocks import Blocks
from score import Score
from enemies import Enemies


class Collisions:
    """ This class stores all the the information needed for collisions and interactions between blocks, enemies and
    Mario"""
    def __init__(self, mario: Mario, score: Score):
        # It creates a score and mario variables to interact with them
        self.score = score
        self.mario = mario
        # This is a variable with all the blocks of the level
        self.blocks = [Blocks(200, 168, "coin"), Blocks(280, 168, "normal"), Blocks(296, 168, "coin"),
                       Blocks(312, 168, "normal"), Blocks(328, 168, "mushroom"), Blocks(344, 168, "normal"),
                       Blocks(312, 112, "coin"), Blocks(416, 208, "pipe down"), Blocks(416, 192, "pipe up"),
                       Blocks(544, 208, "pipe down"), Blocks(544, 200, "pipe down"), Blocks(544, 184, "pipe up"),
                       Blocks(736, 208, "pipe down"), Blocks(736, 192, "pipe down"), Blocks(736, 176, "pipe up"),
                       Blocks(928, 208, "pipe down"), Blocks(928, 192, "pipe down"), Blocks(928, 184, "pipe down"),
                       Blocks(928, 168, "pipe up"), Blocks(992, 112, "normal"), Blocks(1008, 112, "normal"),
                       Blocks(1024, 112, "normal"), Blocks(1088, 168, "normal"), Blocks(1104, 168, "mushroom"),
                       Blocks(1120, 168, "normal"), Blocks(1232, 168, "normal"), Blocks(1248, 168, "coin"),
                       Blocks(1264, 168, "normal"), Blocks(1264, 112, "normal"), Blocks(1280, 112, "normal"),
                       Blocks(1296, 112, "normal"), Blocks(1312, 112, "normal"), Blocks(1328, 112, "normal"),
                       Blocks(1344, 112, "normal"), Blocks(1360, 112, "normal"), Blocks(1376, 112, "normal"),
                       Blocks(1344, 208, "unbreakable"), Blocks(1360, 208, "unbreakable"), Blocks(1376, 208, "unbreakable"),
                       Blocks(1360, 192, "unbreakable"), Blocks(1376, 192, "unbreakable"), Blocks(1376, 176, "unbreakable"),
                       Blocks(1440, 208, "unbreakable"), Blocks(1456, 208, "unbreakable"), Blocks(1472, 208, "unbreakable"),
                       Blocks(1440, 192, "unbreakable"), Blocks(1456, 192, "unbreakable"), Blocks(1440, 176, "unbreakable"),
                       Blocks(1372, 112, "normal"), Blocks(1488, 112, "normal"), Blocks(1504, 112, "normal"),
                       Blocks(1520, 112, "normal"), Blocks(1536, 112, "normal"), Blocks(1552, 112, "coin"),
                       Blocks(1568, 168, "normal"), Blocks(1584, 168, "normal"), Blocks(1552, 168, "normal"),
                       Blocks(1648, 208, "unbreakable"), Blocks(1664, 208, "unbreakable"), Blocks(1680, 208, "unbreakable"),
                       Blocks(1696, 208, "unbreakable"), Blocks(1712, 208, "unbreakable"), Blocks(1728, 208, "unbreakable"),
                       Blocks(1664, 192, "unbreakable"), Blocks(1680, 192, "unbreakable"), Blocks(1696, 192, "unbreakable"),
                       Blocks(1712, 192, "unbreakable"), Blocks(1728, 192, "unbreakable"), Blocks(1680, 176, "unbreakable"),
                       Blocks(1696, 176, "unbreakable"), Blocks(1712, 176, "unbreakable"), Blocks(1728, 176, "unbreakable"),
                       Blocks(1696, 160, "unbreakable"), Blocks(1712, 160, "unbreakable"), Blocks(1728, 160, "unbreakable"),
                       Blocks(1760, 144, "unbreakable"), Blocks(1744, 144, "unbreakable"), Blocks(1760, 128, "unbreakable"),
                       Blocks(1744, 112, "unbreakable"), Blocks(1744, 128, "unbreakable"), Blocks(1712, 144, "unbreakable"),
                       Blocks(1744, 160, "unbreakable"), Blocks(1744, 176, "unbreakable"), Blocks(1744, 192, "unbreakable"),
                       Blocks(1744, 208, "unbreakable"), Blocks(1760, 112, "unbreakable"), Blocks(1728, 128, "unbreakable"),
                       Blocks(1728, 144, "unbreakable"), Blocks(1760, 160, "unbreakable"), Blocks(1760, 176, "unbreakable"),
                       Blocks(1760, 192, "unbreakable"), Blocks(1760, 208, "unbreakable"), Blocks(1876, 208, "unbreakable"),
                       Blocks(1876, 192, "flag down"), Blocks(1876, 176, "flag down"), Blocks(1876, 160, "flag down"),
                       Blocks(1876, 144, "flag down"), Blocks(1876, 128, "flag down"), Blocks(1876, 112, "flag down"),
                       Blocks(1876, 96, "flag down"), Blocks(1876, 80, "flag down"), Blocks(1870, 64, "flag"),
                       Blocks(1876, 48, "flag up")]
        # To create a variable with all the floor blocks we use a while loop
        n = 0
        self.floor = []
        for i in range(200):
            self.floor.append(Floor(n, 240))
            self.floor.append(Floor(n, 224))
            n += 16
        # We also create a list with all the enemies
        self.enemies = [Enemies(random.randint(1, 4), 168, self.mario), Enemies(random.randint(1, 4), 268, self.mario),
                        Enemies(random.randint(1, 4), 768, self.mario), Enemies(random.randint(1, 4), 1368, self.mario),
                        Enemies(random.randint(1, 4), 1668, self.mario)]
        # We create this variable that will be useful for Mario's collisions
        self.up_down = False

    def contact(self):
        """ This method checks if Mario is touching any kind of block"""
        # It sets as False a touch variable
        touch = False
        for object in self.blocks:
            # It applies this condition that checks if Mario if touching a block to all the blocks in the block list
            # If it is true, it turns the touch variable into True
            if self.mario.x + self.mario.width >= object.x and self.mario.x <= object.x + object.width and (
                    (self.mario.y <= object.y + object.height and self.mario.y >= object.y) or (
                    self.mario.y + self.mario.height <= object.y + object.height and self.mario.y +
                    self.mario.height >= object.y)):
                touch = True
        # It returns the touch variable, that will allow to check if Mario is touching any block
        return touch

    def interactions(self):
        """ This method will allow Mario to collide and interact with every block, so it will include a lot of
        conditions depending on if Mario is big and on what part of the block it touches, so that it can set its
        position in order not to touch the block"""
        # We divide into two case to establish the interactions: big Mario and small Mario
        # If Mario is big
        if not self.mario.big:
            for object in self.blocks:
                # And the type of the block is not one of those below
                if object.type != "flag down" and object.type != "flag" and object.type != "flag up" and \
                        object.type != "mushroom object":
                    # If Mario touches a block from the left
                    if object.x <= self.mario.x + self.mario.width <= object.x + 10 and \
                            (object.y + object.height >= self.mario.y >= object.y or object.y + object. height
                             > self.mario.y + self.mario.height > object.y):
                        # We change Mario's x so that it doesn't touch the object anymore
                        self.mario.x = object.x - self.mario.width
                        # And we turn this False, which will disable the up/down collisions
                        self.up_down = False
                    # If Mario touches the block from the right
                    elif object.x + object.width - 10 <= self.mario.x <= object.x + object.width and \
                            (object.y + object.height >= self.mario.y >= object.y
                             or object.y + object.height > self.mario.y + self.mario.height > object.y):
                        # We change Mario's x so that it doesn't touch the object anymore
                        self.mario.x = object.x + object.width
                        # And we turn this False, which will disable the up/down collisions
                        self.up_down = False
                    else:
                        # If Mario doesn't touch a block neither from the left nor from the right we turn up_down True
                        self.up_down = True
                        # If up_down is true the vertical collisions will be enabled
                    if self.up_down:
                        # When up_down is True and Mario touches a block
                        if (object.y <= self.mario.y + self.mario.height <= object.y + object.height or object.y <=
                            self.mario.y <= object.y + object.height) and (object.x <= self.mario.x + self.mario.width
                                                                           <= object.x + object.width or object.x
                                                                           <= self.mario.x <= object.x + object.width):
                            # If Mario is going up, it touches the block from below
                            if self.mario.going_up:
                                # So it will change its y position and its speed to 0, so that it falls
                                self.mario.speed = 0
                                self.mario.y = object.y + object.height
                                # If the object is a coin block Mario will obtain a coin and points
                                if object.type == "coin":
                                    object.type = "broken"
                                    self.score.coins += 1
                                    self.score.score += 200
                                    # If the object is a mushroom block it will generate a mushroom
                                elif object.type == "mushroom":
                                    object.type = "broken"
                                    self.blocks.append(Blocks(object.x, object.y - 16, "mushroom object"))
                            # If Mario is going down it touches the block from above
                            elif not self.mario.going_up:
                                # So it will change its position, and turn the relative_y into 0, to be able to jump
                                self.mario.relative_y = 0
                                self.mario.y = object.y - self.mario.height
                                self.mario.jumping = True
                # If the object is a mushroom and Mario touches it
                elif object.type == "mushroom object":
                    if (object.y <= self.mario.y + self.mario.height <= object.y + object.height or object.y <=
                        self.mario.y <= object.y + object.height) and (object.x <= self.mario.x + self.mario.width <=
                                                                       object.x + object.width or object.x <=
                                                                       self.mario.x <= object.x + object.width):
                        # Mario will be big, obtain 1000 points and the mushroom will disappear
                        self.blocks.remove(object)
                        self.score.score += 1000
                        self.mario.big = True
                        self.mario.height += 16
                # If the object is a part of the flag and Mario touches it
                elif object.type == "flag down" or object.type == "flag" or object.type == "flag up":
                    if object.x <= self.mario.x + self.mario.width <= object.x + 10 and self.mario.y + \
                            self.mario.height <= 208:
                        # Mario will obtain points depending on its y position
                        if self.mario.y >= 160:
                            self.score.score += 1000
                        elif self.mario.y >= 112:
                            self.score.score += 2000
                        elif self.mario.y >= 80:
                            self.score.score += 3000
                        elif self.mario.y < 80:
                            self.score.score += 4000
                        self.mario.y = 256 - 32 - self.mario.height
                        # The end variable will turn True, so Mario will have won
                        self.score.end = True
        # If Mario is big
        elif self.mario.big:
            for object in self.blocks:
                # And the type of block is none of those below
                if object.type != "flag down" and object.type != "flag" and object.type != "flag up" and object.type \
                        != "mushroom object":
                    # If Mario touches a block from the left
                    if object.x <= self.mario.x + self.mario.width <= object.x + 10 and \
                            (object.y + object.height >= self.mario.y >= object.y or object.y + object. height >
                             self.mario.y + self.mario.height > object.y or
                             (object.y + object.height <= self.mario.y + self.mario.height and object.y >= self.mario.y)):
                        # It will change its position and make up_down False
                        self.mario.x = object.x - self.mario.width
                        self.up_down = False
                    # If Mario touches a block from the right
                    elif object.x + object.width - 10 <= self.mario.x <= object.x + object.width and \
                            (object.y + object.height >= self.mario.y >= object.y or object.y + object.height >
                             self.mario.y + self.mario.height > object.y or
                             (object.y + object.height <= self.mario.y + self.mario.height and object.y >= self.mario.y)):
                        # It will change its position and make up_down False
                        self.mario.x = object.x + object.width
                        self.up_down = False
                    else:
                        # If Mario doesn't touch a block neither from the left nor from the right we turn up_down True
                        self.up_down = True
                    # If up_down is True the vertical collisions will be enabled
                    if self.up_down:
                        # If it touches a block
                        if (object.y <= self.mario.y + self.mario.height <= object.y + object.height or
                            object.y <= self.mario.y <= object.y + object.height) \
                                and (object.x <= self.mario.x + self.mario.width <= object.x + object.width or
                                     object.x <= self.mario.x <= object.x + object.width):
                            # ANd Mario is going up it touches it from below
                            if self.mario.going_up:
                                # Mario changes its position and turns it speed to 0, in order to fall
                                self.mario.speed = 0
                                self.mario.y = object.y + object.height
                                if object.type == "coin":
                                    # If it is a coin block Mario will obtain points and a coin
                                    object.type = "broken"
                                    self.score.coins += 1
                                    self.score.score += 200
                                elif object.type == "normal":
                                    # If it is a normal block Mario will obtain points and break the coin
                                    self.blocks.remove(object)
                                    # We break the coin by removing it to the list of blocks
                                    self.score.score += 50
                                elif object.type == "mushroom":
                                    # If the block is a mushroom block a mushroom will appear on the block
                                    object.type = "broken"
                                    self.blocks.append(Blocks(object.x, object.y - 16, "mushroom object"))
                            # If Mario isn't going up it is above the block
                            elif not self.mario.going_up:
                                # Mario will change its position and turn its relative_y to 0, to be able to jump again
                                self.mario.relative_y = 0
                                self.mario.y = object.y - self.mario.height
                                self.mario.jumping = True
                # If the object is a mushroom and Mario touches it
                elif object.type == "mushroom object":
                    if (object.y <= self.mario.y + self.mario.height <= object.y + object.height or
                        object.y <= self.mario.y <= object.y + object.height) and\
                            (object.x <= self.mario.x + self.mario.width <= object.x + object.width or
                             object.x <= self.mario.x <= object.x + object.width):
                        # Mario obtain 1000 points and the mushroom will disappear
                        self.blocks.remove(object)
                        self.score.score += 1000
                # If the object is a part of the flag and Mario touches it
                elif object.type == "flag down" or object.type == "flag" or object.type == "flag up":
                    if object.x <= self.mario.x + self.mario.width <= object.x + 10 and self.mario.y \
                            + self.mario.height <= 208:
                        # Mario will obtain points depending on its y position
                        if self.mario.y >= 160:
                            self.score.score += 1000
                        elif self.mario.y >= 112:
                            self.score.score += 2000
                        elif self.mario.y >= 80:
                            self.score.score += 3000
                        elif self.mario.y < 80:
                            self.score.score += 4000
                        self.mario.y = 256 - 32 - self.mario.height
                        # The end variable will turn True, so Mario will have won
                        self.score.end = True

    def fall(self):
        """ This function makes Mario fall when it is not touching any block"""
        # It checks that Mario is not jumping and not touching any block with the contact method
        if not self.contact() and self.mario.y < 256 - 32 - self.mario.height and not self.mario.jumping:
            # It turns the speed into 0, makes the relative_y different to 0 and makes jumping True
            self.mario.speed = 0
            self.mario.relative_y += 1
            self.mario.jumping = True

    def enemies_collision(self):
        """ This function makes enemies collide with blocks and change their direction"""
        for object in self.blocks:
            for enemy in self.enemies:
                # It is different for the koopa troopas because their height is different
                if enemy.type == 1:
                    # If the enemy touches the object from the left its direction will change to right
                    if object.x + object.width - 5 <= enemy.x <= object.x + object.width and \
                            enemy.y + 7 <= object.y <= enemy.y + 9:
                        enemy.dir = "right"
                        # If the enemy touches the object from the right its direction will turn to left
                    elif object.x <= enemy.x + enemy.width <= object.x + 5 and enemy.y + 7 <= object.y <= enemy.y + 9:
                        enemy.dir = "left"
                # For the goomba it works exactly the same but its easier because it is as tall as the objects
                else:
                    if object.x + object.width - 5 <= enemy.x <= object.x + object.width and\
                            enemy.y == object.y:
                        enemy.dir = "right"
                    elif object.x <= enemy.x + enemy.width <= object.x + 5 and enemy.y == object.y:
                        enemy.dir = "left"

    def die_mario(self):
        """ This method makes Mario lose a live when it touches an enemy from a side"""
        for enemy in self.enemies:
            # The conditions when Mario is big will be slightly different
            if self.mario.big:
                # If the enemy is a koopa troopa and Mario touches it from a side
                if enemy.type == 1 and (enemy.x <= self.mario.x + self.mario.width <= enemy.x + enemy.width or enemy.x
                                        <= self.mario.x <= enemy.x + enemy.width) and enemy.y <= self.mario.y + 8:
                    # Mario will turn small again
                    # Its position will change in order to able able to avoid dying again
                    self.mario.sprite = constants.MARIO_SPRITE
                    self.mario.x = 30
                    self.mario.y = 125
                    self.mario.big = False
                    self.mario.height -= 16
                # If the enemy is a goomba it will happen exactly the same
                elif (enemy.x <= self.mario.x + self.mario.width <= enemy.x + enemy.width or enemy.x
                      <= self.mario.x <= enemy.x + enemy.width) and enemy.y <= self.mario.y + 16:
                    # Mario will turn small and change its position
                    self.mario.sprite = constants.MARIO_SPRITE
                    self.mario.x = 30
                    self.mario.y = 125
                    self.mario.big = False
                    self.mario.height -= 16
            # If Mario is small and touches an enemy from the side
            elif not self.mario.big:
                # If the enemy is a koopa troopa
                if enemy.type == 1 and (enemy.x <= self.mario.x + self.mario.width <= enemy.x + enemy.width or enemy.x
                                        <= self.mario.x <= enemy.x + enemy.width) and enemy.y <= self.mario.y - 8:
                    # Mario will lose a life and change its position
                    self.mario.x = 30
                    self.mario.y = 125
                    self.score.lives -= 1
                # And if the enemy is a goomba it will happen exactly the same
                elif (enemy.x <= self.mario.x + self.mario.width <= enemy.x + enemy.width or enemy.x
                      <= self.mario.x <= enemy.x + enemy.width) and enemy.y <= self.mario.y:
                    self.mario.x = 30
                    self.mario.y = 125
                    self.score.lives -= 1

    def kill_enemies(self):
        """ This method allows Mario to kill an enemy by jumping over it"""
        for enemy in self.enemies:
            # It divides again the cases of big and small Mario
            # If Mario is not big
            if not self.mario.big:
                # And it touches a koopa troopa from above
                if enemy.type == 1 and enemy.y - 10 <= self.mario.y <= enemy.y - 6 and enemy.x - 15 <= self.mario.x \
                        <= enemy.x + 15:
                    # The enemy dies (disappears) by being removed to the list
                    self.enemies.remove(enemy)
                    # Mario obtains 100 points
                    self.score.score += 100
                # The same happens with goomba
                elif enemy.y - 18 <= self.mario.y <= enemy.y - 14 and enemy.x - 15 <= self.mario.x <= enemy.x + 15:
                    self.enemies.remove(enemy)
                    self.score.score += 100
            # And the same happens with big mario
            elif self.mario.big:
                if enemy.type == 1 and enemy.y - 26 <= self.mario.y <= enemy.y - 22 and enemy.x - 15 <= self.mario.x \
                        <= enemy.x + 15:
                    self.enemies.remove(enemy)
                    self.score.score += 100
                elif enemy.y - 34 <= self.mario.y <= enemy.y - 30 and enemy.x - 15 <= self.mario.x <= enemy.x + 15:
                    self.enemies.remove(enemy)
                    self.score.score += 100