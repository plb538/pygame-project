from src.entities.entity import Entity


class Player(Entity):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	# For testing
	def update(self):
		x, y = self.get_position()
		self.set_position(x + 1, y)