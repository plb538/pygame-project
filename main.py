#!/usr/bin/python3

import traceback

import pygame as pg
from src.game.game import Game

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
