import numpy as np

if __name__ == '__main__':
	# part 1
	with open('input', 'r') as f:
		lines = f.readlines()

	lines = [list(line.replace('\n', '')) for line in lines]
	lines = [[int(i) for i in line] for line in lines]
	table = np.array(lines)
	means = np.mean(table, axis = 0)

	major = list(means > 0.5)
	minor = list(means <= 0.5)
	gamma = int(''.join([str(int(i)) for i in major],), 2)
	epsilon = int(''.join([str(int(i)) for i in minor],), 2)

	print('The power consumption of the submarine is ', gamma * epsilon)

	# part 2

	# find oxygen generator rating
	oxy_table = table
	digit = 0
	while len(oxy_table) > 1:
		means = np.mean(oxy_table, axis = 0)
		major = list(means >= 0.5)
		oxy_table = oxy_table[np.where(oxy_table[:, digit] == major[digit])]
		digit += 1
	oxy_rate = int(''.join([str(int(i)) for i in oxy_table[0]],), 2)

	# find co2 scrubber rating
	co2_table = table
	digit = 0
	while len(co2_table) > 1:
		means = np.mean(co2_table, axis = 0)
		minor = list(means >= 0.5)
		co2_table = co2_table[np.where(co2_table[:, digit] != minor[digit])]
		digit += 1
	co2_rate = int(''.join([str(int(i)) for i in co2_table[0]],), 2)

	print('The life support rating of the submarine is :', co2_rate * oxy_rate)
