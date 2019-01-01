#!/usr/bin python3
#
# Advent of Code 2018 - Day 5
#

import re

INPUTFILE = 'input.txt'

def load_input(infile):
	characters = []
	with open(infile, 'r') as fp:
		while True:
			char = fp.read(1)
			if not char:
				break
			if not char.isspace():
				characters.append(char)
		return characters

# PART 1
def part1(characters):
	print('Units before=', len(characters))
	i = 0
	while i < len(characters):
		if i + 1 < len(characters):
			c = characters[i]
			n = characters[i+1]
			# First we must know if the letter is the same, so ignore case.
			if re.match(c, n, flags=re.IGNORECASE):
				# Then again without ignorecase to check if case/'polarity' is different.
				if not re.match(c, n):
					del characters[i]
					del characters[i]
					# If we deleted some characters, maybe we should take a few steps back to analyze more characters.
					# 1 step back plus 1 since we're about to increment at end of loop.
					# This is a bit sloppy. It gives the right answer, but if you change it to for instance i -= 3 it gives the wrong answer.
					i -= 2
		i += 1
	print('PART 1=', len(characters))

	
		
if __name__ == '__main__':
	input = load_input(INPUTFILE)
	part1(input)