from src.managers.game_state_manager import GameStateManager

import pygame as pg


class Game:

	def __init__(self):
		self._running = True
		self._clk = pg.time.Clock()
		self._fps = 60
		self._game_title = "Game"
		self._screen_size = (800, 600)
		self._screen = pg.display.set_mode(self._screen_size)
		pg.display.set_caption(self._game_title)

		# Test
		GameStateManager.instance().set_game_state('test_state')

	def _handle_event(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				self._running = False
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					self._running = False

	def _update(self):
		GameStateManager.instance().update()

	def _draw(self):
		GameStateManager.instance().draw(self._screen)

	def start(self):
		while self._running:
			self._handle_event()
			self._update()
			self._draw()
			self._clk.tick(self._fps)
			pg.display.update()
		print("Exiting game loop.")
