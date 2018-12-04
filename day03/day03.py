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

	def intersectionAsRectangle(self, other):
		intersection = Rectangle(self.id + other.id)
		left_edge = right_edge = top_edge = bottom_edge = 0
		x_overlap = y_overlap = 0
		# Is other.left contained in self?
		if self.left() <= other.left() <= self.right():
			left_edge = other.left()
			right_edge = min(self.right(), other.right())
		# Is other.right contained in self?
		elif self.left() <= other.right() <= self.right():
			right_edge = other.right()
			left_edge = max(self.left(), other.left())
		x_overlap = right_edge - left_edge

		# Is other.top contained in self?
		if self.top() <= other.top() <= self.bottom():
			top_edge = other.top()
			bottom_edge = min(self.bottom(), other.bottom())
		# Is other.bottom contained in self?
		elif self.top() <= other.bottom() <= self.bottom():
			bottom_edge = other.bottom()
			top_edge = max(self.top(), other.top())
		y_overlap = bottom_edge - top_edge

		if x_overlap and y_overlap:
			intersection.x = left_edge
			intersection.y = top_edge
			intersection.w = right_edge - left_edge
			intersection.h = bottom_edge - top_edge
			return intersection
		else:
			return False
		


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

	# Find overlap between two rectangles, and mark that area as a 1 in grid.
	grid = [[0 for x in range(1000)] for y in range(1000)]

	for rect1 in list_rectangles:
		for rect2 in list_rectangles:
			if rect1 is not rect2:
				intersection = rect1.intersectionAsRectangle(rect2)
				if intersection:
					for i in range(intersection.left(), intersection.right()):
						for j in range(intersection.top(),intersection.bottom()):
							grid[i][j] = 1

	# Count up the 1s in the grid:
	for x in grid:
		for y in x:
			output += y
			

	print("PART 1: " + str(output))

# PART 2
def part2(arg):
	output = ""
	print("PART 2: " + str(output))

if __name__ == '__main__':
	print("EXAMPLE 1: ")
	r1 = Rectangle("#1", 1, 3, 4, 4)
	r2 = Rectangle("#2", 3, 1, 4, 4)
	r3 = Rectangle("#3", 5, 5, 2, 2)
	print(r1.intersectionAsRectangle(r2))
	print(r1.intersectionAsRectangle(r3))
	print(r2.intersectionAsRectangle(r3))
	example1 = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]	
	part1(example1)
	print("EXAMPLE 2: ")
	#part2(example2_input)
	print("END OF EXAMPLES")
	input = load_input(INPUTFILE)
	part1(input)
	part2(input)
