import pygame
import random
from SET_NUMBERS import *

class Platform:
	def __init__(self, x, y):
		self._x = x
		self._y = y
		self._img = PLATFORM_IMG

class Platforms:
	def __init__(self, n):
		self._n = n # number of platforms
		coordinates = self.generate_random_coordinates(n) # n random coordinates sorted by y value
		self._list_of_platforms = [(Platform(coordinates[i][0], coordinates[i][1])) for i in range(len(coordinates))] # list of platforms
		self._move = 0 # total shift distance
		self._t2 = 1 # shift animation time

	@staticmethod
	def generate_random_coordinates(n):
		# (5, 25) -> (405, 655) 5, 85...405 || 25, 55.....655
		choice = [(i+j%7, j) for i in range(5, 485, 80) for j in range(0, 685, 30)] 
		random.shuffle(choice)
		final_choice = choice[:n]

		# if the lowest one isn't low enough
		if final_choice[-1][1] < WIN_HEIGHT - 45:
			final_choice.append((choice[n][0], WIN_HEIGHT - 45))
			n += 1

		final_choice.sort(key = lambda c: c[1]) # sort by y value

		# if the distance between any 2 platforms is too short
		added = 0 
		for i in range(n-1):
			if final_choice[i+added+1][1] - final_choice[i+added][1] > 180: 
				low = final_choice[i+added+1][1]
				while low - final_choice[i+added][1] > 180:
					final_choice.insert(i+added+1, (choice[n+1][0], final_choice[i+added][1] + 90))  
					if low - final_choice[i+added+1][1] <= 180:
						added += 1
						break
					added += 1

		# if doodle won't be able to jump high enought once shift
		while final_choice[0][1] + WIN_HEIGHT - final_choice[-1][1] > 180:
			final_choice.insert(0, (choice[n+1][0], final_choice[0][1]/2))
			n += 1
		return final_choice

	def check_collide(self, doodle):
		doodle_mask = pygame.mask.from_surface(doodle._img)

		for platform in self._list_of_platforms:

			platform_mask = pygame.mask.from_surface(platform._img)

			offset = (round(platform._x - doodle._x), round(platform._y - doodle._y))

			collide = doodle_mask.overlap(platform_mask, offset)

			if collide and doodle._t < 0:
				if platform._y < WIN_HEIGHT - 50: 
					dy = WIN_HEIGHT - 50 - platform._y
					self._move = dy
					self._t2 = 1
					doodle._move = dy
					doodle._t = 1
					doodle._t2 = 1
					doodle._score += round(dy)
				else:
					doodle._t = 1
				break

	def shift(self, endgaming = False):
		if self._move > 0 and self._t2 > 0:
	
			if endgaming:
				new_list = []
				for platform in self._list_of_platforms:
					platform._y -= self._move/FPS
					if platform._y > 0:
						new_list.append(platform)
				self._list_of_platforms = new_list

			else:
				x_choices = [i for i in range(5, 485, 80)] # possible x for the new platform
				for index, platform in enumerate(self._list_of_platforms):
					platform._y += self._move/FPS
					if platform._y > WIN_HEIGHT - 7.5: # if it is half gone (15 / 2)
						platform._x = x_choices[random.randint(0, len(x_choices) - 1)]
						platform._y = 7.5
					
		
			self._t2 -= 1/FPS
			if self._t2 < 0:
				self._move = 0