from game_object_type import GameObjectType
from sprite import Sprite


class Food(Sprite):
	def __init__(self, x_pos, y_pos, filename):
		super().__init__(x_pos, y_pos, filename)
		self.type = GameObjectType.FOOD
