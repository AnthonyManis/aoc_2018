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
	charlist = characters.copy()
	i = 0
	while i < len(charlist):
		deleted_characters = False
		if i + 1 < len(charlist):
			c = charlist[i]
			n = charlist[i+1]
			# First we must know if the letter is the same, so ignore case.
			if re.match(c, n, flags=re.IGNORECASE):
				# Then again without ignorecase to check if case/'polarity' is different.
				if not re.match(c, n):
					del charlist[i]
					del charlist[i]
					deleted_characters = True

	
		# If we deleted a character, please take a step back to see if the deletion cascades.
		if deleted_characters:
			i -= 1
		else:
			i += 1
	return (len(charlist))

def part2(characters):
	characters_string = ''.join(characters)

	# In essence, iterate through alphabet removing that character from the list,
	# Run part1 analysis on the list and record the smallest resulting polymer & corresponding letter.
	# Print the smallest length (we don't care about which letter it is for some reason).

	# For every letter in the alphabet.
	minimum_length = len(characters)
	best_letter = None
	ascii_letter = ord('a')
	for i in range(26):
		letter = chr(ascii_letter)
		# Purge the letter from the string.
		charlist = list(re.sub(letter, '', characters_string, flags=re.IGNORECASE))
		poly_len = part1(charlist)
		if poly_len < minimum_length:
			minimum_length = poly_len
			best_letter = letter

		# Loop increment
		ascii_letter += 1

	print('PART 2 =', minimum_length)
	print('Best letter was', best_letter)
	
		
if __name__ == '__main__':
	input = load_input(INPUTFILE)
	print('PART 1 =', part1(input))
	part2(input)
