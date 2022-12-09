# Define the Piece class
class Piece:
  def __init__(self, color, position):
    self.color = color
    self.position = position

  # Method for moving a piece to a new position
  def move(self, new_position):
    self.position = new_position

# Define the Pawn class, which inherits from the Piece class
class Pawn(Piece):
  def __init__(self, color, position):
    # Call the parent class's constructor
    super().__init__(color, position)

# Define the Rook class, which inherits from the Piece class
class Rook(Piece):
  def __init__(self, color, position):
    # Call the parent class's constructor
    super().__init__(color, position)

# Define the Bishop class, which inherits from the Piece class
class Bishop(Piece):
  def __init__(self, color, position):
    # Call the parent class's constructor
    super().__init__(color, position)

# Define the Knight class, which inherits from the Piece class
class Knight(Piece):
  def __init__(self, color, position):
    # Call the parent class's constructor
    super().__init__(color, position)

# Define the Queen class, which inherits from the Piece class
class Queen(Piece):
  def __init__(self, color, position):
    # Call the parent class's constructor
    super().__init__(color, position)

# Define the King class, which inherits from the Piece class
class King(Piece):
  def __init__(self, color, position):
    # Call the parent class's constructor
    super().__init__(color, position)

# Define the Board class
class Board:
  def __init__(self):
    # Initialize the board with the starting positions of the pieces
    self.board = [
      ["R", "N", "B", "Q", "K", "B", "N", "R"],
      ["P", "P", "P", "P", "P", "P", "P", "P"],
      [" ", " ", " ", " ", " ", " ", " ", " "],
      [" ", " ", " ", " ", " ", " ", " ", " "],
      [" ", " ", " ", " ", " ", " ", " ", " "],
      [" ", " ", " ", " ", " ", " ", " ", " "],
      ["p", "p", "p", "p", "p", "p", "p", "p"],
      ["r", "n", "b", "q", "k", "b", "n", "r"]
    ]

  # Method for printing the board
  def print_board(self):
    for row in self.board:
      print(" ".join(row))

# Create a Board object and print it
board = Board()
board.print_board()
