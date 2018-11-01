import pygame as pg
from src.managers.entity_manager import EntityManager as em
from src.managers.game_state_manager import GameStateManager as gsm


class Game:
	_running = True
	_clk = pg.time.Clock()
	_fps = 30
	_game_title = "Game"
	_screen = None
	_screen_size = (800,600)
	_screen_background_color = (255,255,255)

	def __init__(self):
		self._screen = pg.display.set_mode(self._screen_size)

		pg.display.set_caption(self._game_title)

		gsm.instance().init()
		em.instance().init()

		# Test
		gsm.instance().set_game_state('test_state')


	def _handle_event(self):
		for e in pg.event.get():
			if e.type == pg.QUIT:
				self._running = False
			if e.type == pg.KEYDOWN:
				if e.key == pg.K_ESCAPE:
					self._running = False

	def _update(self):
		gsm.instance().update()

	def _draw(self):
		gsm.instance().draw(self._screen)

	def start(self):
		while self._running:
			self._handle_event()
			self._update()
			self._draw()
			self._clk.tick(self._fps)
			pg.display.update()
		print("Exiting game loop.")

