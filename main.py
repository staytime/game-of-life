#! /usr/bin/python3.4


import pygame
import game
import random

GAME_WIDTH, GAME_HEIGHT = 120, 80
GAME_CELL_SIZE = 10
pygame.init()

if __name__ == '__main__':
	screen = pygame.display.set_mode((
		GAME_WIDTH * GAME_CELL_SIZE,
		GAME_HEIGHT * GAME_CELL_SIZE))
	pygame.display.set_caption('Game of Life')
	screen.fill((255, 255, 255))

	def gridlize(x, y):
		x -= (x % GAME_CELL_SIZE)
		y -= (y % GAME_CELL_SIZE)
		return x, y

	world = game.world()
	world.init((GAME_WIDTH, GAME_HEIGHT))

	done = False
	run = True
	addRandom = False
	goNext = False


	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:	
				done = True

			if event.type == pygame.KEYDOWN:
				key = event.key

				if key == pygame.K_q:
					done = True
				elif key == pygame.K_w:
					run = not run
				elif key == pygame.K_r:
					addRandom = not addRandom
				elif key == pygame.K_e:
					goNext = True
					run = False

			if event.type == pygame.MOUSEBUTTONUP:
				if not run:
					x, y = event.pos
					x, y = gridlize(x, y)
					local = x / GAME_CELL_SIZE, y / GAME_CELL_SIZE

					for __, life in world.getCells(local):
						if life is None:
							world.add(local)
						else:
							world.remove(local)

		title = 'Game of Life'
		if not run:
			title = 'Game of Life (pause)'

		pygame.display.set_caption(title)

		if run or goNext:
			world.update()
			goNext = False

			if addRandom:
				for i in range(int(GAME_HEIGHT * GAME_WIDTH / 1000) * 5):
					def __():
						return (random.randint(0, GAME_WIDTH - 1),
							random.randint(0, GAME_HEIGHT - 1))

					while not world.add(__()):
						pass

		
		screen.fill((255, 255, 255))
		
		for (x, y), life in world.getCells():

			color = (0, 128, 255)
			if life > 1:
				color = (219, 70, 78)

			pygame.draw.rect(
				screen,
				color,
				(
					x * GAME_CELL_SIZE, y * GAME_CELL_SIZE,
					GAME_CELL_SIZE, GAME_CELL_SIZE))

		if pygame.mouse.get_focused():
			x, y = pygame.mouse.get_pos()
			x, y = gridlize(x, y)

			pygame.draw.rect(
				screen,
				(0, 0, 0),
				(
					x, y,
					GAME_CELL_SIZE, GAME_CELL_SIZE),
				1)
			

			

		pygame.display.flip()
		pygame.time.wait(int(1000 / 10))
