from src.game_states.game_state import GameState
from src.managers.entity_manager import EntityManager as em
from src.managers.map_manager import MapManager as mm
from src.common import constants as c

import pygame as pg
class TestState(GameState):

	def __init__(self):
		super(TestState, self).__init__()

		mm.instance().\
			load_map('test')

		# Eventually we will create a sprite manager but for now
		# just use the path to a sprite image
		self.p1 = em.instance()\
			.create_entity(
			'player',
			x_pos=350, y_pos=100, mass=100,
			width=128, length=128,
			sprite="{}/adventurer-idle-00.png".format(c.SPRITE_PATH)
		)

		em.instance()\
			.create_entity(
			'platform',
			x_pos=400, y_pos=500, mass=100,
			width=328, length=128,
			sprite="{}/goku.jpg".format(c.SPRITE_PATH)
		)

	# This is just here for now until
	# a map manager is created.
	def update(self):
		super(TestState, self).update()
		hits = pg.sprite.spritecollide(
			self.p1, em.instance().entity_groups['platform'], False)
		if hits:
			x, y = self.p1.get_position()
			self.p1.set_position(x, hits[0].rect.top)

	def draw(self, screen):
		screen.fill((0, 5, 0))
		super(TestState, self).draw(screen)
