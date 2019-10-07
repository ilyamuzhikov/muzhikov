#!/usr/bin/env python3

import sys
import pygame as pg
from pygame.locals import *

pg.init()

SIZE = width, height = 640, 480
speedball = [4, 4]
speedsled = [0, 0]
BGCOLOR = 90, 90, 90

screen = pg.display.set_mode(SIZE)

sled = pg.image.load("sled.png")
ball = pg.image.load("ball.png")

ballrect = ball.get_rect()
sledrect = sled.get_rect()

sledrect.move_ip((20, 10))
ballrect.move_ip((320, 240))

while True:
	for e in pg.event.get():
		if e.type == pg.QUIT:
			pg.quit()
			sys.exit()

		if e.type == KEYDOWN:
			if e.key == K_UP: speedsled[1] = -10
			if y > 480:
				y = 480
			if e.key == K_DOWN: speedsled[1] = 10
			if y < 0:
				y = 0
		if e.type == KEYUP:
			if e.key == K_UP or e.key == K_DOWN: speedsled[1] = 0

	ballrect = ballrect.move(speedball)
	sledrect = sledrect.move(speedsled)
	
	if sledrect.colliderect(ballrect):
		speedball[0] = -speedball[0]

	if ballrect.left < 0 or ballrect.right > width:
		speedball[0] = -speedball[0]
	if ballrect.top < 0 or ballrect.bottom > height:
		speedball[1] = -speedball[1]

	screen.fill(BGCOLOR)
	screen.blit(ball, ballrect)
	screen.blit(sled, sledrect)
	pg.display.update()
	pg.time.delay(20)
