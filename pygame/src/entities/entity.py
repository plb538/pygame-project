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
		self._width = width
		self._length = length
		self._mass = mass

		self.set_image(sprite)
		if not width and not length:
			width = 0
			length = 0
		self.set_entity_size(width, length)

		self._pos = vec()
		if not x_pos:
			x_pos = 0
		if not y_pos:
			y_pos = 0
		self.set_position(x_pos, y_pos)

		self._vel = vec()
		if not x_vel:
			x_vel = 0
		if not y_vel:
			y_vel = 0
		self.set_velocity(x_vel, y_vel)

		self._acc = vec()
		if not x_acc:
			x_acc = 0
		if not y_acc:
			y_acc = 0
		self.set_acceleration(x_acc, y_acc)

	def set_position(self, x_pos, y_pos):
		self._pos.x = x_pos
		self._pos.y = y_pos
		self.rect.midbottom = self._pos

	def get_position(self):
		return self._pos

	def set_velocity(self, x_vel, y_vel):
		self._vel.x = x_vel
		self._vel.y = y_vel

	def get_velocity(self):
		return self._vel

	def set_acceleration(self, x_acc, y_acc):
		self._acc.x = x_acc
		self._acc.y = y_acc

	def get_acceleration(self):
		return self._acc

	def set_mass(self, mass):
		self._mass = mass

	def get_mass(self):
		return self._mass

	def set_entity_size(self, width, length):
		try:
			self._width = width
			self._length = length
			self.image = pg.transform.scale(self.image, (width, length))
			self.rect = self.image.get_rect()
		except Exception as ex:
			raise Exception(
				"Failed to set image size: %s"
				% ex
			)

	def get_entity_size(self):
		return self._width, self._length

	def set_image(self, sprite_path):
		self.image = pg.image.load(sprite_path).convert()

