from src.managers.entity_manager import EntityManager as em

class GameState:

	def __init__(self):
		pass

	def update(self):
		em.instance().update()

	def draw(self, screen):
		screen.fill((230,25,20))
		em.instance().draw(screen)
