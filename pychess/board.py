BOARD_DEFAULT_ROWS = 8
BOARD_DEFAULT_COLS = 8


class Board:
	"""
	This class is responsible for storing all the chess pieces and their position.
	"""

	def __init__(self, rows = BOARD_DEFAULT_ROWS, cols = BOARD_DEFAULT_COLS):
		"""
		Generates board with given number of rows and cols.
		"""
		pass

	def add_piece(self, piece, position):
		"""
		Adds a piece at the given position.
		"""
		pass

	def remove_piece(self, position):
		"""
		Removes the piece at the given position.
		"""
		pass

	def move_piece(self, piece, from_position, to_position):
		"""
		Moves the piece from a given position to other position.
		"""
		pass

	def get_piece(self, position):
		"""
		Returns the piece at the given position.
		"""
		pass