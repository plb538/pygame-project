import pygame as pg
vec = pg.math.Vector2

# Base class from all entities
class Entity(pg.sprite.Sprite):

	def __init__(self, x_pos=None, y_pos=None, mass=None,
				 width=None, length=None, sprite=None,
				 x_vel=None, y_vel=None, x_acc=None, y_acc=None):
		super().__init__()
		# Every Sprite requires these fields
		self.image = None
		self.rect = None
		self.width = width
		self.length = length
		self.mass = mass

		# NOTE: Need to move to physics.
		self.set_image(sprite)
		if not width and not length:
			width = 0
			length = 0
		self.set_entity_size(width, length)

		self.pos = vec()
		if not x_pos:
			x_pos = 0
		if not y_pos:
			y_pos = 0
		self.set_position(x_pos, y_pos)

		self.vel = vec()
		if not x_vel:
			x_vel = 0
		if not y_vel:
			y_vel = 0
		self.set_velocity(x_vel, y_vel)

		self.acc = vec()
		if not x_acc:
			x_acc = 0
		if not y_acc:
			y_acc = 0
		self.set_acceleration(x_acc, y_acc)

	def set_position(self, x_pos, y_pos):
		self.pos.x = x_pos
		self.pos.y = y_pos
		self.rect.midbottom = self.pos

	def get_position(self):
		return self.pos

	def set_velocity(self, x_vel, y_vel):
		self.vel.x = x_vel
		self.vel.y = y_vel

	def get_velocity(self):
		return self.vel

	def set_acceleration(self, x_acc, y_acc):
		self.acc.x = x_acc
		self.acc.y = y_acc

	def get_acceleration(self):
		return self.acc

	def set_mass(self, mass):
		self.mass = mass

	def get_mass(self):
		return self.mass

	def set_entity_size(self, width, length):
		try:
			self.width = width
			self.length = length
			self.image = pg.transform.scale(self.image, (width, length))
			self.rect = self.image.get_rect()
		except Exception as ex:
			raise ex

	def get_entity_size(self):
		return self.width, self.length

	def set_image(self, sprite_path):
		self.image = pg.image.load(sprite_path).convert()

