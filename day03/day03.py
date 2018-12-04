#!/usr/bin python3
#
# Advent of Code 2018 - Day 3
#

import re

INPUTFILE = 'input.txt'

def load_input(infile):
	lines = []
	with open(infile, 'r') as fp:
		for line in fp:
			line = line.strip()
			if line:
				lines.append(line)

	return lines

# PART 1
class Rectangle:
	"""A rectangle in four numbers... maybe a few more."""

	def __init__(self, id = None, x = None, y = None , w = None , h = None):
		self.id = id
		self.x = int(x)
		self.y = int(y)
		self.w = int(w)
		self.h = int(h)

	def __str__(self):
		result = str(self.id) + " (" + str(self.x) + "," + str(self.y) + ") "
		result += str(self.w) + "x" + str(self.h)
		return result
	
	def left(self):
		return self.x
	
	def right(self):
		return self.x + self.w
	
	def top(self):
		return self.y

	def bottom(self):
		return self.y + self.h

	def area(self):
		return self.w * self.h

	def containsPoint(self, point_x, point_y):
		if self.left() < point_x <= self.right():
			if self.top() < point_y <= self.bottom():
				return True
		
		return False

	def intersectionAsRectangle(self, other):
		# Is other.left contained in self?
			# How much overlap is there?
		# Is other.right contained in self?
			# How much overlap is there?


		# Is other.top contained in self?
			# How much overlap is there?
		# Is other.bottom contained in self?
			# How much overlap is there?


def part1(arg):
	output = ""
	# Construct a list of rectangles from the input lines.
	list_rectangles = []
	for line in arg:
		line = re.sub('[@:]', '', line)
		id,coords,dimensions = line.split()
		x,y = coords.split(',')
		w,h = dimensions.split('x')

		r = Rectangle(id, x, y, w, h)
		list_rectangles.append(r)

	# Find overlap between two rectangles, and mark that area as a 1 in grid.
	grid = [[0 for x in range(1000)] for y in range(1000)]
	

	print("PART 1: " + str(output))

# PART 2
def part2(arg):
	output = ""
	print("PART 2: " + str(output))

if __name__ == '__main__':
	print("EXAMPLE 1: ")
	#part1(example1_input)
	print("EXAMPLE 2: ")
	#part2(example2_input)
	print("END OF EXAMPLES")
	input = load_input(INPUTFILE)
	part1(input)
	part2(input)
