from src.game_states.game_state import GameState
from src.managers.entity_manager import EntityManager as em

class TestState(GameState):

	def __init__(self):
		super(TestState, self).__init__()

		self.p = em.instance()\
			.create_entity(
			'player',
			x_pos=200, y_pos=200, mass=100,
			width=64, length=64,
			sprite="/home/plb538/Code/python/pygame/resources/goku.jpg"
		)
