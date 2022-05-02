import pygame
import random
from SET_NUMBERS import *
class Doodle:
	def __init__(self, x, y):
		self._x = x # doodle's coordinate
		self._y = y
		self._xvel = 0 # doodle's x, y velocity
		self._yvel = 0
		self._flip = False # whether the doodle face right
		self._jump = False # whether the doodle jumps!

		self._t = 1 # jump animation time
		self._move = 0 # total shift distance
		self._t2 = 0 # shift animation time

		self._score = 0 # final score
		self._img = DOODLE_IMG[0]

	def jump(self, endgaming):
		self._yvel = SPEED * self._t
		self._x += self._xvel
		if not endgaming:
			self._y += self._yvel
		self._t -= 1/FPS

		# if doodle need to bend its kneels to jump
		if abs(self._t - 0) > 0.8:
			if self._flip == True:
				self._img = DOODLE_JUMP_IMG[1]
			else:
				self._img = DOODLE_JUMP_IMG[0]
		else:
			if self._flip == True:
				self._img = DOODLE_IMG[1]
			else:
				self._img = DOODLE_IMG[0]

		# if jump through right or left boundary
		if self._x > WIN_WIDTH:
			self._x = -50
		elif self._x < -50:
			self._x = WIN_WIDTH

	def shift(self):
		if self._move > 0 and self._t2 > 0:
			self._y += self._move/FPS
			self._t2 -= 1/FPS
			if self._t2 < 0:
				self._t2 = 0
				self._move = 0