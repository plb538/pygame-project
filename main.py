#!/usr/bin/env python3

from src.game.game import Game

import pygame as pg
import traceback


if __name__ == "__main__":
	try:
		pg.init()
		g = Game()
		g.start()
	except Exception:
		traceback.print_exc()
		raise
	finally:
		pg.quit()
		quit()
