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
		acc_vec = vec(0, 2) # Gravity. Move to physics.
		acc = 2 # Run speed.
		friction = -0.2
		if keys[pg.K_LEFT]:
			acc_vec.x -= acc
		if keys[pg.K_RIGHT]:
			acc_vec.x += acc
		if keys[pg.K_UP]:
			acc_vec.y -= acc
		if keys[pg.K_DOWN]:
			acc_vec.y += acc

		self.set_acceleration(acc_vec.x, acc_vec.y)
		vel = self.get_velocity()
		acc_vec += vel * friction
		vel += acc_vec
		self.set_velocity(vel.x, vel.y)
		pos = self.get_position()
		pos += vel
		self.set_position(pos.x, pos.y)

