import numpy as np

if __name__ == '__main__':
	# part 1
	table = np.loadtxt('input', dtype = int)
	diff = table[1:] - table[:-1]
	print('There is', len(diff[diff > 0]), 'increased depth measured')

	# part 2
	window_length = 3
	cumul_table = np.zeros(len(table) - window_length + 1, dtype = int)
	for i in range(window_length):
		start = i
		stop = len(table) + i - window_length
		cumul_table += table[start:(stop + 1)]

	diff = cumul_table[1:] - cumul_table[:-1]
	print('There is', len(diff[diff > 0]),
		f'increased depth measured (given a window of {window_length})')
