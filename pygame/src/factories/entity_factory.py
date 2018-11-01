from src.decorators.singleton import Singleton
from src.entities.player import Player

@Singleton
class EntityFactory:

	_entity_types = (
		PLAYER
	) = (
		'player'
	)

	def create_entity(self, entity, **kwargs):
		try:
			if entity == self.PLAYER:
				return Player(**kwargs)
		except Exception as ex:
			print(ex)
			raise

