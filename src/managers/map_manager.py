from src.decorators.singleton import Singleton
from src.maps.map import Map

@Singleton
class MapManager:

	@staticmethod
	def init():
		print("Initializing MapManager.")

	def load_map(self, map):
		try:
			pass
		except Exception:
			raise

