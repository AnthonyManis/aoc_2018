#!/usr/bin python3
#
# Advent of Code 2018 - Day 3
#

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
def part1(arg):
	output = ""
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
	print(input)
	part1(input)
	part2(input)
