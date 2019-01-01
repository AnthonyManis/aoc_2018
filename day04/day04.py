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

	number_of_minutes = 60
	# Dict of guard number:list of minutes
	guard_dict = {}

	# Iterate through all the events and respond to each one in kind.
	# Date & time comes first on the line, so we're sorting to traverse in chronological order. Good!
	lines.sort()
	for line in lines:
		# New shift happening, set guard on duty & awake.
		new_shift_match = re.search('(?<=Guard #).*(?=begins shift)', line)
		if new_shift_match:
			guard_on_duty = new_shift_match.group()
			# New guard needs a new list to record sleepy minutes.
			if guard_on_duty not in guard_dict:
				guard_dict[guard_on_duty] = [0] * number_of_minutes

		# Now handle events such as waking/sleeping.
		event_match = re.search('(\d{2}):(\d{2})(.*)', line)
		hour = event_match.group(1)
		minute = event_match.group(2)
		if 'asleep' in event_match.group(3):
			sleep_start_minute = int(minute)
			#print(str(hour) + ':' + str(minute),'guard ' + str(guard_on_duty) + 'falls asleep')
		# Luckily, a guard always wakes up before the end shift event is received,
		# so we can use the wake event to record the entire sleep duration in the list.
		if 'wakes' in event_match.group(3):
			sleep_end_minute = int(minute)
			#print(str(hour) + ':' + str(minute),'guard ' + str(guard_on_duty) + 'wakes up')
			print('guard ' + str(guard_on_duty) + ' slept from ' + str(sleep_start_minute) + ' til ' + str(sleep_end_minute))


	# For each guard we need to know:
	#  1 Total minutes slept
	#  2 Minute they slept the most
	

if __name__ == '__main__':
	input = load_input(INPUTFILE)
	part1(input)
