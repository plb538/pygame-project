from src.managers.game_state_manager import GameStateManager

import pygame as pg


class Game:

	def __init__(self):
		self.running = True
		self.clk = pg.time.Clock()
		self.fps = 60
		self.game_title = "Game"
		self.screen_size = (800, 600)
		self.screen = pg.display.set_mode(self.screen_size)
		pg.display.set_caption(self.game_title)

		# Test
		GameStateManager.instance().set_game_state('test_state')

	def handle_event(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.running = False
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					self.running = False

	def update(self):
		GameStateManager.instance().update()

	def draw(self):
		GameStateManager.instance().draw(self.screen)

	def start(self):
		while self.running:
			self.handle_event()
			self.update()
			self.draw()
			self.clk.tick(self.fps)
			pg.display.update()
		print("Exiting game loop.")
