from src.decorators.singleton import Singleton
from src.factories.game_state_factory import GameStateFactory


@Singleton
class GameStateManager:

	#game_states = []

	cur_game_state = None

	@staticmethod
	def init():
		print("Initializing GameStateManager.")

	def update(self):
		self.cur_game_state.update()

	def draw(self, screen):
		self.cur_game_state.draw(screen)

	def set_game_state(self, game_state):
		try:
			if self.cur_game_state:
				del self.cur_game_state
			new_game_state = GameStateFactory.instance().create_game_state(game_state)
			self.cur_game_state = new_game_state
		except Exception:
			raise
