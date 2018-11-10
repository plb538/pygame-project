from src.entities.entity import Entity
import pygame as pg


class Player(Entity):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	# This is just here for now until
	# an event manager is created.
	def update(self):
		x, y = self.get_position()
		dx = 0
		dy = 0
		if pg.key.get_pressed()[pg.K_LEFT]:
			dx = -10
		if pg.key.get_pressed()[pg.K_RIGHT]:
			dx = 10
		if pg.key.get_pressed()[pg.K_UP]:
			dy = -10
		if pg.key.get_pressed()[pg.K_DOWN]:
			dy = 10

		self.set_position(x+dx, y+dy)


