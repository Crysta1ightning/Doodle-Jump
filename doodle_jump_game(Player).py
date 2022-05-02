import pygame
import time
import random
from SET_NUMBERS import *
from doodle_Player import Doodle
from platforms_Player import Platforms

def initialize():

	running = True
	endgaming = False
	gameover = False
	platforms = Platforms(n=INIT_PLATFORM_NUM)
	doodle = Doodle(x=platforms._list_of_platforms[-1]._x, y=platforms._list_of_platforms[-1]._y - 65) # spawn at the lowest platform

	return running, endgaming, gameover, doodle, platforms

def draw_update(doodle, platforms, score):
	WIN.blit(BG_IMG, (0, 0))
	
	for platform in platforms._list_of_platforms:
		WIN.blit(platform._img, (platform._x, platform._y))
	
	WIN.blit(doodle._img, (doodle._x, doodle._y))

	score_text = FONT.render(f"Score: {score:<5}", 1, (0, 0, 0))
	WIN.blit(score_text, (WIN_WIDTH - 10 - score_text.get_width(), 10))
	pygame.display.update()

def main():
	running, endgaming, gameover, doodle, platforms = initialize()
	while running:
		CLOCK.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if not gameover:
					if event.key == pygame.K_a:
						doodle._xvel = -2
						doodle._flip = True
					elif event.key == pygame.K_d:
						doodle._xvel = 2
						doodle._flip = False
					elif event.key == pygame.K_s:
						doodle._xvel = 0
				if gameover:
					if event.key == pygame.K_y:
						running, endgaming, gameover, doodle, platforms = initialize()
					elif event.key == pygame.K_n:
						running = False
			
		# gaming
		if not gameover:
			platforms.check_collide(doodle)
			doodle.jump(endgaming = endgaming)
			doodle.shift()
			platforms.shift(endgaming = endgaming)
			draw_update(doodle, platforms, doodle._score)

			if doodle._y > WIN_HEIGHT - 50 and endgaming == False:
				endgaming = True # start to end game
				platforms._move = WIN_HEIGHT
				platforms._t2 = 2
				for platform in platforms._list_of_platforms:
					platform._y += 100
				doodle._y = WIN_HEIGHT - 100
				doodle._move = 100
				doodle._t2 = 2

			if platforms._list_of_platforms == [] and endgaming:
				gameover = True

		# show final score
		elif gameover:
			WIN.blit(BG_IMG, (0, 0))
			final_score_text = FONT.render(f"FINAL SCORE: {doodle._score}", 1, (0, 0, 0))
			WIN.blit(final_score_text, (WIN_WIDTH/2 - final_score_text.get_width()/2, WIN_HEIGHT/2 - final_score_text.get_height()/2))
			play_again_text = FONT.render(f"Play Again? (Y/N)", 1, (0, 0, 0))
			WIN.blit(play_again_text, (WIN_WIDTH/2 - play_again_text.get_width()/2, WIN_HEIGHT/2 - play_again_text.get_height()/2\
			+ final_score_text.get_height() + 10))
			pygame.display.update()


if __name__ == '__main__':
	pygame.init()
	main()

