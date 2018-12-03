#!/usr/bin python3
#
# Advent of Code 2018 - Day 2
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

# Example
def example1():
    print("EXAMPLE: ")
# PART 1
def part1(input):
    result = ""
    print("PART 1: " + str(result))

# PART 2
def part2(input):
    result = ""
    print("PART 2: " + str(result))

if __name__ == '__main__':
    example1()
    input = load_input(INPUTFILE)
    part1(input)
    part2(input)
