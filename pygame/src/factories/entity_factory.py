from src.decorators.singleton import Singleton
from src.entities.player import Player
from src.entities.platform import Platform
from src.entities.enemy import Enemy


@Singleton
class EntityFactory:

	_entity_types = (
		PLAYER,
		PLATFORM,
		ENEMY
	) = (
		'player',
		'platform',
		'enemy'
	)

	def create_entity(self, entity, **kwargs):
		try:
			if entity == self.PLAYER:
				return Player(**kwargs)
			if entity == self.PLATFORM:
				return Platform(**kwargs)
			if entity == self.ENEMY:
				return Enemy(**kwargs)
		except Exception as ex:
			print(ex)
			raise

