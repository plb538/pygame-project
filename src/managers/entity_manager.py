from src.decorators.singleton import Singleton
from src.factories.entity_factory import EntityFactory

import pygame as pg

@Singleton
class EntityManager:

	entity_groups = {
		key: pg.sprite.Group()
		for key in EntityFactory.instance().entity_types
	}

	@staticmethod
	def init():
		print("Initializing EntityManager.")

	def update(self):
		for k, v in self.entity_groups.items():
			v.update()

	def draw(self, screen):
		for k, v in self.entity_groups.items():
			v.draw(screen)

	def create_entity(self, entity_type, **kwargs):
		try:
			entity = EntityFactory.instance().create_entity(entity_type, **kwargs)
			if entity:
				self.add_to_entity_group(entity, entity_type)
			return entity
		except Exception as ex:
			raise ex

	def add_to_entity_group(self, entity, entity_type):
		self.entity_groups[entity_type].add(entity)
