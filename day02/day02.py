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

# PART 1
def part1(box_ids):
    # key: box id, value: dict of character occurrence counts
    box_stats = {}
    for box in box_ids:
        # Store occurrences of each letter for this box id here
        occurrences = {}
        # list of characters in the box id, in order?
        characters = list(box)
        for c in characters:
            if c in occurrences:
                occurrences[c] += 1
            else:
                occurrences[c] = 1

            box_stats[box] = occurrences
        
    # Now find matches
    match_count = {}
    for key in box_stats:
        for i in range(1,len(key)):
            if i in box_stats[key].values():
                if i in match_count:
                    match_count[i] += 1
                else:
                    match_count[i] = 1
        
    print(match_count)
    checksum = match_count[2] * match_count[3]
    print("PART 1: " + str(checksum))

# PART 2
# Process the character arrays in parallel, comparing chars.
# If the chars are different, keep a count of how many differences are found.
# If the chars are identical, shove em into an output string.
def part2(box_ids):
    output = ""
    for box1 in box_ids:
        for box2 in box_ids:
            if box1 != box2:
                print(box1)
                print(box2)

    print("PART 2: " + str(output))

if __name__ == '__main__':
    print("EXAMPLE1: ")
    example1_input = [ 'abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab' ]
    part1(example1_input)
    print("END OF EXAMPLES")
    input = load_input(INPUTFILE)
    part1(input)
    part2(input)
