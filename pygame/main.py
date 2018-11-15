#!/usr/bin/python3

import pygame as pg
from src.game import game

if __name__ == "__main__":
	try:
		pg.init()
		g = game.Game()
		g.start()
	except Exception as ex:
		print(ex)
		raise
	finally:
		pg.quit()
		quit()
