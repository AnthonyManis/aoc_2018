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

	def __init__(self, id = None, x = 0, y = 0, w = 0 , h = 0):
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

def part1(arg):
	output = 0
	# Construct a list of rectangles from the input lines.
	list_rectangles = []
	for line in arg:
		line = re.sub('[@:]', '', line)
		id,coords,dimensions = line.split()
		x,y = coords.split(',')
		w,h = dimensions.split('x')

		r = Rectangle(id, x, y, w, h)
		list_rectangles.append(r)

	grid = [[0 for x in range(1000)] for y in range(1000)]
	
	# Add 1 to each space in the grid occupied by a rectangle.
	for rect in list_rectangles:
		for x in range(rect.left(), rect.right()):
			for y in range(rect.top(), rect.bottom()):
				grid[x][y] += 1
			
	# Count up the 1s in the grid:
	for x in grid:
		for y in x:
			if y > 1:
				output += 1

	print("PART 1: " + str(output))
	
	# Check each rectangle to see if the grid has a 1 in it for all the spaces in that rect.
	single_claim_rect_id = ""
	for rect in list_rectangles:
		conflict = False
		for x in range(rect.left(), rect.right()):
			for y in range(rect.top(), rect.bottom()):
				if grid[x][y] > 1:
					conflict = True
		if not conflict:
			print(rect.id)	
			single_claim_rect_id = rect.id
	
	print("PART 2: ", single_claim_rect_id)

if __name__ == '__main__':
	print("EXAMPLE 1: ")
	r1 = Rectangle("#1", 1, 3, 4, 4)
	r2 = Rectangle("#2", 3, 1, 4, 4)
	r3 = Rectangle("#3", 5, 5, 2, 2)
	r4 = Rectangle("#4", 0, 0, 10, 10)
	r5 = Rectangle("#5", 9, 9, 1, 1)
	example1 = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2", "#4 @ 0,0: 10x10", "#5 @ 9,9: 1x1"]
	part1(example1)
	print("EXAMPLE 2: ")
	print("END OF EXAMPLES")
	input = load_input(INPUTFILE)
	part1(input)
