from src.managers.entity_manager import EntityManager

# Base class for all game states
class GameState:

	def __init__(self):
		pass

	def update(self):
		EntityManager.instance().update()

	def draw(self, screen):
		EntityManager.instance().draw(screen)
