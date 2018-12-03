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
class Rectangle:
	"""A rectangle in four numbers... maybe a few more."""

	def __init__(self, x = None, y = None , w = None , h = None):
		self.x = x
		self.y = y
		self.w = w
		self.h = h

	def __str__(self):
		result = "(x, y): (" + str(self.x) + ", " + str(self.y) + ")"
		result += "\n"
		result += "(w, h): (" + str(self.w) + ", " + str(self.h) + ")"
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


def part1(arg):
	output = ""
	test = Rectangle(7, 5, 2, 3)
	test2 = Rectangle()
	print("A dead ass rectangle: ")
	print(str(test2))
	print(str(test2.area()))
	print("A less-so dead ass rectangle: ")
	print(str(test))
	print(str(test.area()))
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
	part1(input)
	part2(input)
