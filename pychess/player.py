class Player:
	"""
	This class represents one player in the game.
	"""

	def __init__(self, name, color):
		"""
		Initializes a new player with given name, color and chess pieces.
		"""
		self.name = name
		self.color = color
		self.pieces = set()

	def add_piece(self, piece):
		"""
		Adds a chess piece to player pieces. 
		"""
		pass

	def remove_piece(self, piece):
		"""
		Removes a chess piece from player pieces.
		"""
		pass