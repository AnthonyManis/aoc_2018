#!/usr/bin python3
#
# Advent of Code 2018 - Day 6
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

coords = {}
def labelCoords(lines):
	# Don't do it twice.
	if coords:
		return
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

def findGridSize():
	# Get lowest and highest x and y coordinates so we can just make a grid.
	low_x = high_x = coords['A'][0]
	low_y = high_y = coords['A'][1]
	for x, y in coords.values():
		low_x = x if x < low_x else low_x
		low_y = y if y < low_y else low_y
		high_x = x if x > high_x else high_x
		high_y = y if y > high_y else high_y

	return (low_x, low_y), (high_x, high_y)

def calculateDistanceBetween(x1, y1, x2, y2):
	distance = 0
	distance += abs(x2 - x1)
	distance += abs(y2 - y1)
	return distance

# PART 1
def part1(lines):

	labelCoords(lines)

	(_, _), (high_x, high_y) = findGridSize()

	# It's acceptable to waste some space rather than deal with offsets and oob indices.
	# So we'll start the 2D list at (0, 0)
	grid = [ ['0' for y in range(high_y + 1)] for x in range(high_x + 1) ]

	# For each space in the grid, get its distance to every node.
	# Keep track of the shortest distance, and labels that have that distance.
	for x in range(len(grid)):
		for y in range(len(grid[0])):
			shortest_distance = None
			shortest_labels = []
			for label in coords:
				distance = calculateDistanceBetween(x, y, coords[label][0], coords[label][1])
				# New shortest, reset shortest_labels to single element list.
				if shortest_distance == None or distance < shortest_distance:
					shortest_distance = distance
					shortest_labels = [label]
				# If it's a tie, we append another label to the list.
				elif distance == shortest_distance:
					shortest_labels.append(label)
					

			if len(shortest_labels) > 1:
				grid[x][y] = '.'
			else:
				grid[x][y] = shortest_labels[0]
	
	# Now for the list of labels. Eliminate any label that exists on the grid border.
	# These labels are "unbounded", so they don't count.
	# The remaining labels in the list will all be bounded with a finite area.
	valid_coords = copy.deepcopy(coords)
	for x in range(len(grid)):
		# Top
		label = grid[x][0]
		if label in valid_coords:
			del valid_coords[label]

		# Bottom
		label = grid[x][-1]
		if label in valid_coords:
			del valid_coords[label]
			
	for y in range(len(grid[0])):
		# Left
		label = grid[0][y]
		if label in valid_coords:
			del valid_coords[label]
		
		# Right
		label = grid[-1][y]
		if label in valid_coords:
			del valid_coords[label]

	# Alternative way to visualize grid: Don't show infinite spaces or dots.
	#for x in range(len(grid)):
	#	for y in range(len(grid[0])):
	#		label = grid[x][y]
	#		if label not in valid_coords:
	#			grid[x][y] = ' '

	printGrid(grid)

	# Compute and print largest area.
	areas = {}
	largest = 0
	for label in valid_coords:
		areas[label] = 0
		for x in range(len(grid)):
			for y in range(len(grid[0])):
				if grid[x][y] == label:
					areas[label] += 1
		if areas[label] > largest:
			largest = areas[label]
			largest_label = label

	print('PART 1=' + str(largest) + ' for label ' + largest_label)

def part2(lines, threshold):

	labelCoords(lines)

	(_, _), (high_x, high_y) = findGridSize()

	# Make a grid with the running total score of each coordinate.
	grid_scores = [ [0 for y in range(high_y)] for x in range(high_x) ]

	# For each position in the grid, calculate it's distance to each point, and sum them for the score.
	for x in range(len(grid_scores)):
		for y in range(len(grid_scores[0])):
			score = 0
			for label in coords:
				score += calculateDistanceBetween(x, y, coords[label][0], coords[label][1])
			grid_scores[x][y] = score

	# Find the coordinates that meet the criteria.
	# Less than threshold.
	area = 0
	for x in range(len(grid_scores)):
		for y in range(len(grid_scores[0])):
			if grid_scores[x][y] < threshold:
				area += 1
	print('PART 2=' + str(area))
				

	return

if __name__ == '__main__':
	input = load_input(INPUTFILE)
	part1(input)
	part2(input, 10000)
