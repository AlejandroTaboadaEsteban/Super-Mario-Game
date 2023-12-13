from board import Board
import pyxel

# In this variable we import all the game information from board, and introduce the size of the screen
board = Board(256, 256)

# With these three commands we run the program, starting from the variable set before
pyxel.init(board.width, board.height,)
pyxel.load("assets/resource.pyxres")
pyxel.run(board.update, board.draw)