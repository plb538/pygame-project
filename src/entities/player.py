from src.entities.entity import Entity
import pygame as pg
vec = pg.math.Vector2


class Player(Entity):

	def __init__(self, **kwargs):
		super(Player, self).__init__(**kwargs)

	# This is just here for now until
	# an event manager is created.
	def update(self):
		keys = pg.key.get_pressed()
		acc = vec(0, 2)
		ACC = 2
		FRICTION = -0.2
		if keys[pg.K_LEFT]:
			acc.x -= ACC
		if keys[pg.K_RIGHT]:
			acc.x += ACC
		if keys[pg.K_UP]:
			acc.y -= ACC
		if keys[pg.K_DOWN]:
			acc.y += ACC

		self.set_acceleration(acc.x, acc.y)
		vel = self.get_velocity()
		acc += vel * FRICTION
		vel += acc
		self.set_velocity(vel.x, vel.y)
		pos = self.get_position()
		pos += vel
		self.set_position(pos.x, pos.y)

