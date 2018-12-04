#!/usr/bin python3
#
# Advent of Code 2018 - Day 1
#

INPUTFILE = 'input.txt'

def load_input(infile):
	lines = []
	with open(infile, 'r') as fp:
		for line in fp:
			line = line.strip()
			line = int(line)
			if line:
				lines.append(line)

		return lines

# Example
def example1():
	input = ['+1', '+1', '+1']
	expected = 3
	frequency = 0
	for freq_change in input:
		frequency += int(freq_change)
	
	print("Example: " + str(input) + " Expected: " + str(expected) + " Result: " + str(frequency))

# PART 1
def part1(freq_changes):
	# Frequency always starts at 0
	frequency = 0
	for change in freq_changes:
		frequency += change

	print("PART 1: " + str(frequency))

# PART 2
# Must check for duplicates as we go.
# May need to iterate through list multiple times.
def part2(freq_changes):
	frequency = 0
	counts = { frequency: 1 }
	while counts[frequency] < 2:
		for change in freq_changes:
			frequency += change
			counts[frequency] = 1 + counts.get(frequency, 0)

			if counts[frequency] > 1:
				print("PART 2: " + str(frequency))
				break

if __name__ == '__main__':
	example1()
	input = load_input(INPUTFILE)
	part1(input)
	part2(input)
