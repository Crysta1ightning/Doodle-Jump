import pygame
import neat
import time
import random
import os
from SET_NUMBERS import *
from doodle_AI import Doodle
from platforms_AI import Platforms

def initialize():

	running = True
	platforms = Platforms(n=INIT_PLATFORM_NUM)
	score = 0 
	return running, platforms, score

def genomes_and_nets(genomes, config, platforms):
	nets = []
	ge = []
	doodles = []
	for _, g in genomes:
		net = neat.nn.FeedForwardNetwork.create(g, config)
		nets.append(net)
		doodles.append(Doodle(x=platforms._list_of_platforms[0]._x, y=platforms._list_of_platforms[0]._y - 65)) # spawn at the lowest platform
		g.fitness = 0
		ge.append(g)
	return doodles, nets, ge


def draw_update(doodles, platforms, score):
	WIN.blit(BG_IMG, (0, 0))
	
	for platform in platforms._list_of_platforms:
		WIN.blit(platform._img, (platform._x, platform._y))
	for doodle in doodles:
		WIN.blit(doodle._img, (doodle._x, doodle._y))

	score_text = FONT.render(f"Score: {score:<5}", 1, (0, 0, 0))
	WIN.blit(score_text, (WIN_WIDTH - 10 - score_text.get_width(), 10))
	pygame.display.update()

def main(genomes, config):
	pygame.init()
	running, platforms, score = initialize()
	doodles, nets, ge = genomes_and_nets(genomes, config, platforms)
	while running:
		CLOCK.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		
		for index, doodle in enumerate(doodles):
			dy, score_plus = platforms.check_collide(doodle)
			if dy:
				ge[index].fitness += 1
			score += score_plus
			inputs = []
			for platform in platforms._list_of_platforms[:3]:
				inputs.append(doodle._x - platform._x)
				inputs.append((doodle._y - 65) - platform._y)

			output = nets[index].activate((inputs))

			if output[0] > 0.5:
				doodle._xvel = 2
				doodle._flip = False
			elif output[0] < -0.5:
				doodle._xvel = -2
				doodle._flip = True
			else:
				doodle._xvel = 0

			doodle.jump()
			doodle.shift()

		platforms.shift()

		draw_update(doodles, platforms, score)

		for index, doodle in enumerate(doodles):
			# doodle falls
			if doodle._y > WIN_HEIGHT - 50:
				ge[index].fitness -= 1
				del doodles[index]
				del nets[index]
				del ge[index]

		if len(doodles) == 0:
			running = False



def run(config_path):
	config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
		neat.DefaultSpeciesSet, neat.DefaultStagnation,
		config_path) 
	p = neat.Population(config)
	p.add_reporter(neat.StdOutReporter(True))
	stats = neat.StatisticsReporter()
	p.add_reporter(stats)

	winner = p.run(main, 100)

if __name__ == '__main__':
	run("neat_configuration.txt")