import numpy as np
import pandas as pd

if __name__ == '__main__':
	# part 1
	trajectory = pd.read_csv('input', sep = ' ', names = ['direction', 'value'])
	forward = trajectory.loc[lambda df: df['direction'] == 'forward', :]
	up = trajectory.loc[lambda df: df['direction'] == 'up', :]
	down = trajectory.loc[lambda df: df['direction'] == 'down', :]

	total_forward = sum(forward['value'])
	total_depth = sum(down['value']) - sum(up['value'])
	print('The total forward move is : ', total_forward,
		'and the total depth move is', total_depth,
		'giving a product of', total_depth * total_forward)


