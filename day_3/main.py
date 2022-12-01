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
	converted_gamma = int(''.join([str(int(i)) for i in major],), 2)
	converted_epsilon = int(''.join([str(int(i)) for i in minor],), 2)

	print('The power consumption of the submarine is ', converted_gamma * converted_epsilon)
	