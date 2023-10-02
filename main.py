#!/usr/bin/env python3

from src.game.game import Game

import pygame as pg


if __name__ == "__main__":
	try:
		pg.init()
		game = Game()
		game.start()
	except Exception as ex:
		raise ex
	finally:
		pg.quit()
		quit()
