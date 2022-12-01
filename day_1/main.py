import numpy as np

if __name__ == '__main__':
	# part 1
	table = np.loadtxt('input', dtype = int)
	diff = table[1:] - table[:-1]
	print('There is', len(diff[diff > 0]), 'increased depth measured')
	