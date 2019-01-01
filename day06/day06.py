#!/usr/bin python3
#
# Advent of Code 2018 - Day 4
#

import re
import copy

INPUTFILE = 'input.txt'

def load_input(infile):
	lines = []
	with open(infile, 'r') as fp:
		for line in fp:
			line = line.strip()
			line = line
			if line:
				lines.append(line)

		return lines

# Not super useful if the terminal's width is smaller than len(grid)
def printGrid(grid):
	for y in range(len(grid[0])):
		line_string = ''
		for x in range(len(grid)):
			line_string += grid[x][y]
		print(line_string)
		
# PART 1
def part1(lines):
	coords = {}
	id = 0
	for line in lines:
		x, y = map(int, line.split(','))
		coords[id] = (x,y)
		id += 1

	# Get lowest and highest x and y coordinates so we can just make a grid.
	low_x = high_x = coords[0][0]
	low_y = high_y = coords[0][1]
	for x, y in coords.values():
		low_x = x if x < low_x else low_x
		low_y = y if y < low_y else low_y
		high_x = x if x > high_x else high_x
		high_y = y if y > high_y else high_y

	# Interestingly test input is of size (313,313)
	# We'll have some extra space since the low_x and low_y are greater than 0,
	# but it's acceptable to waste some space rather than deal with offsets and oob indices.
	grid = [ ['0' for y in range(high_y + 1)] for x in range(high_x + 1) ]

	#print('high_x  high_y')
	#print(high_x, high_y)
	#print('len(grid)  len(grid[0])')
	print(len(grid), len(grid[0]))

	grid_count = 0
	for id,node in coords.items():
		print(node[0], node[1])
		grid[node[0]][node[1]] = id
		grid_count += 1
	while grid_count < len(grid) * len(grid[0]):
		pass

	# For each iteration until the grid is full
	# Copy the grid to grid_prime
	# If a space has a letter in it, expand that letter outwards in four directions.
	#  000    0a0
	#  0A0 -> aAa
	#  000    0a0
	# With some exceptions:
	#  0 Don't go out of bounds.
	#  1 If a space is already occupied in grid, don't modify it.
	#  2 If a space is NOT occupied in grid, but IS occupied in grid_prime, then set it to a '.' (neutral for equal distance between nodes)


if __name__ == '__main__':
	input = load_input(INPUTFILE)
	part1(input)
