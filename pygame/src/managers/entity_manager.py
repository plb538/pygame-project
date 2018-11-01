import pygame as pg
from src.decorators.singleton import Singleton
from src.factories.entity_factory import EntityFactory as ef

@Singleton
class EntityManager:

	_entities = pg.sprite.Group()

	@staticmethod
	def init():
		print("Initializing EntityManager.")

	def update(self):
		self._entities.update()

	def draw(self, screen):
		self._entities.draw(screen)

	def create_entity(self, entity, **kwargs):
		try:
			e = ef.instance()\
				.create_entity(entity, **kwargs)
			self._entities.add(e)
			return e
		except Exception as ex:
			raise Exception(
				"Failed to create entity: %s"
				% ex
			)

