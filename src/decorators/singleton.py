
class Singleton:

	def __init__(self, decorated):
		self.decorated = decorated

	def instance(self):
		try:
			return self._instance
		except AttributeError:
			self._instance = self.decorated()
			return self._instance

	def __call__(self):
		raise TypeError('Singletons must be accessed through `instance()`.')

	def __instancecheck__(self, inst):
		return isinstance(inst, self.decorated)
