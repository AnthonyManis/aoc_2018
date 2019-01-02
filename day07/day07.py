#!/usr/bin python3
#
# Advent of Code 2018 - Day 7
#

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

def part1(lines):
	return

if __name__ == '__main__':
	input = load_input(INPUTFILE)
	part1(input)
