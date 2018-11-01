import pygame as pg


class Entity(pg.sprite.Sprite):

	# Every Sprite requires these fields
	image = None
	rect = None

	# These fields are for us
	_x_pos = None
	_y_pos = None
	_mass = None
	_width = None
	_length = None


	def __init__(self, x_pos=None, y_pos=None, mass=None,
				 width=None, length=None, sprite=None):
		super().__init__()
		# Must be defined
		if not width and not length:
			width = 0
			length = 0
		self.set_sprite(sprite)
		self.set_rect_center(width, length)
		self.set_entity_size(width, length)
		if x_pos and y_pos:
			self.set_position(x_pos, y_pos)
		if mass:
			self.set_mass(mass)


	def set_position(self, x_pos, y_pos):
		self._x_pos = x_pos
		self._y_pos = y_pos
		self.rect.x = x_pos
		self.rect.y = y_pos

	def get_position(self):
		return self._x_pos, self._y_pos

	def set_mass(self, mass):
		self._mass = mass

	def get_mass(self):
		return self._mass

	def set_entity_size(self, width, length):
		try:
			if self._width == width and self._length == length:
				return
			else:
				self._width = width
				self._length = length
				self.image = pg.transform.scale(self.image, (width, length))
		except Exception as ex:
			raise Exception(
				"Failed to set image size: %s"
				% ex
			)

	def get_entity_size(self):
		return self._width, self._length

	def set_rect_center(self, width, length):
		self.rect = self.image.get_rect()
		self.rect.center = (width / 2, length / 2)

	def set_sprite(self, sprite_path):
		self.image = pg.image.load(sprite_path).convert()

