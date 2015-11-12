#! /usr/bin/python3


import random
import time

CELL_BORN_STATE = int(1)

class world(object):
	def __init__(self):
		super().__init__()

	def init(self, size):
		self.gameMap = dict()
		w, h = [int(i) for i in size]
		self.size = (w, h)

	def regular(tar):
		try:
			x, y = tar
			w, h = self.size
			return (
				(x + w) % w,
				(y + h) % h)
		except AttributeError as e:
			print("The world obj haven't initialize properly.")
			exit()

	def area(self, x, y):
		for xoffset in range(-1, 2):
			for yoffset in range(-1, 2):
				if (abs(xoffset) + abs(yoffset)) != 0:
					try:
						w, h = self.size
						
						yield (
								(x + w + xoffset) % w,
								(y + h + yoffset) % h
							)

					except AttributeError as e:
						print("The world obj haven't initialize properly.")
						exit()

	def add(self, local):
		x, y = [int(i) for i in local]

		if (x, y) not in self.gameMap:
			self.gameMap[(x, y)] = CELL_BORN_STATE
			return True
		else:
			return False

	def update(self):

		# init work varible
		lifeCounter = dict()

		# update age of the cell
		for local in self.gameMap:
			self.gameMap[local] += 1

		# register cell are already here
		for local in self.gameMap.keys():
			lifeCounter[local] = 0

		# count neighbor
		for (x, y) in self.gameMap.keys():
			for local in self.area(x, y):
				if local in lifeCounter:
					lifeCounter[local] += 1
				else:
					lifeCounter[local] = 1

		# decide the cell life or death
		for local, life in lifeCounter.items():
			if life == 3:
				self.add(local)
			elif life == 2:
				# because not change need here
				pass
			else:
				self.remove(local)

	def getCells(self, tarCell = None):
		try:
			if tarCell is None:
				for local, life in self.gameMap.items():
					yield local, life
			else:
				if tarCell in self.gameMap:
					yield (tarCell, self.gameMap[tarCell])
				else:
					yield (tarCell, None)

		except AttributeError as e:
			print("The world obj haven't initialize properly.")
			exit()

	def remove(self, tarCell):
		try:
			if tarCell in self.gameMap:
				del self.gameMap[tarCell]
		except AttributeError as e:
			print("The world obj haven't initialize properly.")
			exit()


if __name__ == '__main__':
	exit()

