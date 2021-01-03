from src.decorators.singleton import Singleton
from src.factories.game_state_factory import GameStateFactory


@Singleton
class GameStateManager:

	#_game_states = []

	_cur_game_state = None

	@staticmethod
	def init():
		print("Initializing GameStateManager.")

	def update(self):
		self._cur_game_state.update()

	def draw(self, screen):
		self._cur_game_state.draw(screen)

	def set_game_state(self, game_state):
		try:
			if self._cur_game_state:
				del self._cur_game_state
			_game_state = GameStateFactory.instance().create_game_state(game_state)
			self._cur_game_state = _game_state
		except Exception:
			raise


