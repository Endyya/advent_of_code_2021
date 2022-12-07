import numpy as np

def main(part = 1, test = False):
	if test:
		filename = 'inputtest'
	else:
		filename = 'input'

	with open(filename, 'r') as f:
		pos = f.readline()

	pos = [int(i) for i in pos.split(',')]
	possibilities = np.array(range(max(pos) + 1))

	pos_rep = np.repeat(pos, repeats = len(possibilities)).reshape(len(pos), len(possibilities))
	poss_rep = np.repeat(possibilities, repeats = len(pos)).reshape(len(possibilities), len(pos)).T

	if part == 1:
		cost = np.fabs(pos_rep - poss_rep)
	elif part == 2:
		cost = np.fabs(pos_rep - poss_rep)
		cost = cost * (cost + 1) / 2

	cum_cost = np.sum(cost, axis = 0)

	print(int(min(cum_cost)))



if __name__ == '__main__':
	
	#part 1
	main(part = 1)

	#part 2
	main(part = 2)