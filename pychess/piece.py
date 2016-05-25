class Piece:
	"""
	Base class for all chess pieces in the game.
	"""

	def __init__(self, color):
		self.color = color
		self.movements = {}