from src.game_states.game_state import GameState
from src.managers.entity_manager import EntityManager as em


class TestState(GameState):

	def __init__(self):
		super(TestState, self).__init__()

		# Eventually we will create a sprite manager but for now
		# just use the path to a sprite image
		em.instance()\
			.create_entity(
			'player',
			x_pos=200, y_pos=200, mass=100,
			width=64, length=64,
			sprite="/home/plb538/Code/python/pygame/pygame/resources/goku.jpg"
		)


	# This is just here for now until
	# a map manager is created.
	def draw(self, screen):
		screen.fill((230, 25, 20))
		super(TestState, self).draw(screen)
