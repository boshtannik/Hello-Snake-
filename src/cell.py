from src.game_object_type import GameObjectType
from src.sprite import Sprite


class Cell(Sprite):
	def __init__(self, x_pos, y_pos, filename):
		super().__init__(x_pos, y_pos, filename)
		self.number = 0
		self.type = GameObjectType.SNAKE
