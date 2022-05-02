WIN_WIDTH = 500
WIN_HEIGHT = 700
FPS = 120
SPEED = -4 # velocity
INIT_PLATFORM_NUM = 6
BLANK = 45 # y for blank

import pygame
pygame.init()

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

CLOCK = pygame.time.Clock()

FONT = pygame.font.SysFont("comicsans", 30)

BG_IMG = pygame.image.load("background_img_1.png") # 532*850
DOODLE_IMG = [pygame.image.load("doodle_1.png"), ''] 
DOODLE_JUMP_IMG = [pygame.image.load("doodle_1_jump.png"), '']
DOODLE_IMG[0] = pygame.transform.scale(DOODLE_IMG[0], (80, 80))
DOODLE_IMG[1] = pygame.transform.flip(DOODLE_IMG[0], True, False)
DOODLE_JUMP_IMG[0] = pygame.transform.scale(DOODLE_JUMP_IMG[0], (80, 80))
DOODLE_JUMP_IMG[1] = pygame.transform.flip(DOODLE_JUMP_IMG[0], True, False)

PLATFORM_IMG = pygame.image.load("platform_1.png")
PLATFORM_IMG = pygame.transform.scale(PLATFORM_IMG, (80, 15))
PLATFORM2_IMG = pygame.image.load("platform_2.png") # 100*22
PLATFORM2_IMG = pygame.transform.scale(PLATFORM2_IMG, (80, 15))

