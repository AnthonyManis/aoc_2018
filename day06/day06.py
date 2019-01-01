#!/usr/bin python3
#
# Advent of Code 2018 - Day 4
#

import re
import copy
import subprocess

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

# Returns True if the coordinates given by pair are valid indices in the 2D grid.
# Otherwise returns False.
def isInBounds(pair, grid):
	if 0 <= pair[0] < len(grid):
		if 0 <= pair[1] < len(grid[0]):
			return True
	return False

# Modifies gprime to expand the given label into indices denoted by pair.
# If a conflict is detected, expand a '.' instead.
# Returns the number of spaces that became non-zero during the operation.
def expandTo(label, pair, g, gprime):
	if not isInBounds(pair, g):
		return 0

	x = pair[0]
	y = pair[1]
	result = 0
	if g[x][y] == '0':
		if gprime[x][y]  == '0' or gprime[x][y] == label:
			gprime[x][y] = label
			result = 1
		else:
			# Conflict in gprime. Set to dot, but result 0 since we didn't fill a "new" space.
			gprime[x][y] = '.'
			result = 0

	return result
	
# Maybe useful, maybe not. Depends on the visibility of labels chosen.
# Artificially breaking after TERMINAL_COLS columns
TERMINAL_COLS = 200
def printGrid(grid):
	# This is fun... get the width of the terminal in columns,
	# and use that for the printing width of printGrid
	sp = subprocess.Popen(['tput', 'cols'], stdout=subprocess.PIPE)
	(output, err) = sp.communicate()
	TERMINAL_COLS = int(output)

	for y in range(len(grid[0])):
		line_string = ''
		for x in range(min(len(grid), TERMINAL_COLS)):
			line_string += grid[x][y]
		print(line_string)
	
	if len(grid) > TERMINAL_COLS:
		for y in range(len(grid[0])):
			line_string = ''
			for x in range(TERMINAL_COLS, len(grid)):
				line_string += grid[x][y]
			print(line_string)

# PART 1
def part1(lines):
	coords = {}
	# Assign a single-character label to each starting node.
	label_ascii = ord('A')
	for line in lines:
		# Skip non-letter labels.
		label_ascii = 97 if label_ascii == 91 else label_ascii
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
	#  000	  0A0
	#  0A0 -> AAA
	#  000	  0A0
	# With some exceptions:
	#  0 Don't go out of bounds.
	#  1 If a space is already occupied in grid, don't modify it.
	#  2 If a space is NOT occupied in grid, but IS occupied in grid_prime, instead set it to a '.' (neutral for equal distance between nodes)
	# Finally, grid becomes grid prime.
	grid = copy.deepcopy(grid_nodes_only)
	last_grid_count = 0
	while grid_count > last_grid_count:
		last_grid_count = grid_count
		grid_prime = copy.deepcopy(grid)
		for x in range(len(grid)):
			for y in range(len(grid[0])):
				# Expand in all directions if label is nonzero and non-dot.
				label = grid[x][y]
				if label != '0' and label != '.':
					# Left
					grid_count += expandTo(label, (x - 1, y), grid, grid_prime)
					# Up
					grid_count += expandTo(label, (x, y - 1), grid, grid_prime)
					# Right
					grid_count += expandTo(label, (x + 1, y), grid, grid_prime)
					# Down
					grid_count += expandTo(label, (x, y + 1), grid, grid_prime)
		grid = grid_prime

	printGrid(grid)

if __name__ == '__main__':
	input = load_input(INPUTFILE)
	part1(input)
