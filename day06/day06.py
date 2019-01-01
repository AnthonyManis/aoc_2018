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
	
# Maybe useful, maybe not. Depends on the visibility of labels chosen.
# Useless unless the terminal width is >= len(grid)
def printGrid(grid):
	for y in range(len(grid[0])):
		line_string = ''
		for x in range(len(grid)):
			line_string += grid[x][y]
		print(line_string)

# PART 1
def part1(lines):
	coords = {}
	# Assign a single-character label to each starting node.
	label_ascii = ord('A')
	for line in lines:
		label = chr(label_ascii)
		x, y = map(int, line.split(','))
		coords[label] = (x, y)
		# Next label
		label_ascii += 1

	# Get lowest and highest x and y coordinates so we can just make a grid.
	low_x = high_x = coords['A'][0]
	low_y = high_y = coords['A'][1]
	for x, y in coords.values():
		low_x = x if x < low_x else low_x
		low_y = y if y < low_y else low_y
		high_x = x if x > high_x else high_x
		high_y = y if y > high_y else high_y

	# Interestingly test input is of size (313,313)
	# We'll have some extra space since the low_x and low_y are greater than 0,
	# but it's acceptable to waste some space rather than deal with offsets and oob indices.
	grid_nodes_only = [ ['0' for y in range(high_y + 1)] for x in range(high_x + 1) ]

	# Add initial nodes to the grid.
	grid_count = 0
	for label, node in coords.items():
		#print(label, node[0], node[1])
		grid_nodes_only[node[0]][node[1]] = label
		grid_count += 1

	# For each iteration until the grid is full
	# Copy the grid to grid_prime
	# If a space has an id in it, expand that id outwards in four directions.
	# *Notation note: not using upper/lowercase as in example, since we need more labels than just 26.
	#  000    0A0
	#  0A0 -> AAA
	#  000    0A0
	# With some exceptions:
	#  0 Don't go out of bounds.
	#  1 If a space is already occupied in grid, don't modify it.
	#  2 If a space is NOT occupied in grid, but IS occupied in grid_prime, then set it to a '.' (neutral for equal distance between nodes)
	grid = copy.deepcopy(grid_nodes_only)
	while grid_count < len(grid) * len(grid[0]):
		grid_prime = copy.deepcopy(grid_nodes_only)
		break


if __name__ == '__main__':
	input = load_input(INPUTFILE)
	part1(input)
