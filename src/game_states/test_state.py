from src.common import constants as const
from src.game_states.game_state import GameState
from src.managers.entity_manager import EntityManager
from src.managers.map_manager import MapManager

import pygame as pg

class TestState(GameState):

	def __init__(self):
		super(TestState, self).__init__()

		MapManager.instance().load_map('test')

		# Eventually we will create a sprite manager but for now
		# just use the path to a sprite image
		self.p1 = EntityManager.instance().create_entity(
			'player',
			x_pos=351, y_pos=100, mass=100,
			width=128, length=128,
			sprite="{}/adventurer-idle-00.png".format(const.SPRITE_PATH)
		)

		EntityManager.instance().create_entity(
			'platform',
			x_pos=400, y_pos=500, mass=100,
			width=528, length=128,
			sprite="{}/goku.jpg".format(const.SPRITE_PATH)
		)

	# This is just here for now until
	# a map manager is created.
	def update(self):
		super(TestState, self).update()
		hits = pg.sprite.spritecollide(
			self.p1, EntityManager.instance().entity_groups['platform'], False)
		if hits:
			x, y = self.p1.get_position()
			self.p1.set_position(x, hits[0].rect.top)

	def draw(self, screen):
		screen.fill((0, 5, 0))
		super(TestState, self).draw(screen)
