from src.managers.entity_manager import EntityManager as em

# Base class for all game states
class GameState:

	def __init__(self):
		pass

	def update(self):
		em.instance().update()

	def draw(self, screen):
		em.instance().draw(screen)
