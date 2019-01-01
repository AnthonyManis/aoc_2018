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
		# Luckily, a guard always wakes up before the end shift event is received,
		# so we can use the wake event to record the entire sleep duration in the list.
		if 'wakes' in event_match.group(3):
			sleep_end_minute = int(minute)
			# Record a sleep event by incrementing in guard's list.
			for i in range(number_of_minutes):
				if sleep_start_minute <= i < sleep_end_minute:
					guard_dict[guard_on_duty][i] += 1

	# For each guard we need to know:
	#  1 Total minutes slept
	#  2 Minute they slept the most
	best_guard = None
	most_minutes_slept = 0
	for guard_id, sleep_list in guard_dict.items():
		sum_minutes = sum(sleep_list)
		if sum_minutes > most_minutes_slept:
			best_guard = guard_id
			most_minutes_slept = sum_minutes
	print('Best guard #' + str(best_guard), 'Slept for', most_minutes_slept, 'minutes!')

	slept_minute_max = 0
	choice_minute = None
	for i in range(number_of_minutes):
		slept_this_minute = guard_dict[best_guard][i]
		if slept_this_minute > slept_minute_max:
			choice_minute = i
			slept_minute_max = slept_this_minute
	print('Choice Minute:', choice_minute)
	print('Checksum: ', int(best_guard) * int(choice_minute))

	print('Part 2: Now we don\'t care about who the best guard is, just looking for the best minute.')
	sleep_minute_max = 0
	choice_minute = None
	choice_guard = None
	for guard_id, sleep_list in guard_dict.items():
		for i in range(number_of_minutes):
			slept_this_minute = guard_dict[guard_id][i]
			if slept_this_minute > slept_minute_max:
				choice_minute = i
				choice_guard = guard_id
				slept_minute_max = slept_this_minute
	print('Choice guard', choice_guard, 'Choice minute', choice_minute)
	print('Checksum: ', int(choice_guard) * int(choice_minute))
		
if __name__ == '__main__':
	input = load_input(INPUTFILE)
	part1(input)
