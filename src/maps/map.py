
class Map:

	def __init__(self, map_file):
		self._map_file = map_file
		self.parsed_fields = self.parse_map_file(map_file)

	def parse_map_file(self, map_file):
		return {}
