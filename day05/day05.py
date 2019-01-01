#!/usr/bin python3
#
# Advent of Code 2018 - Day 5
#

INPUTFILE = 'input.txt'

def load_input(infile):
	characters = []
	with open(infile, 'r') as fp:
		while True:
			char = fp.read(1)
			if not char:
				print('EOF')
				break
			if not char.isspace():
				characters.append(char)
		return characters

# PART 1
def part1(characters):
	print(characters)
		
if __name__ == '__main__':
	input = load_input(INPUTFILE)
	part1(input)
