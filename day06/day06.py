#!/usr/bin python3
#
# Advent of Code 2018 - Day 4
#

import re

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

	# Technically it's offset by (low_x, low_y), but I'm not sure that I care.
	# Interestingly test input is of size (313,313)
	grid = [ [0 for x in range(high_x - low_x)] for y in range(high_y - low_y) ]


if __name__ == '__main__':
	input = load_input(INPUTFILE)
	part1(input)
