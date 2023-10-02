from src.decorators.singleton import Singleton
from src.game_states.test_state import TestState

@Singleton
class GameStateFactory:

	game_states = (
		TEST_STATE
	) = (
		'test_state'
	)

	def create_game_state(self, game_state):
		try:
			if game_state == self.TEST_STATE:
				return TestState()
		except Exception:
			raise

