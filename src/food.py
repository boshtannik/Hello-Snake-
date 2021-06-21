from src.game_object_type import GameObjectType
from src.sprite import Sprite


class Food(Sprite):
	def __init__(self, x_pos, y_pos):
		super().__init__(x_pos, y_pos, "src/hero.png")
		self.type = GameObjectType.FOOD
