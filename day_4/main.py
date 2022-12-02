import numpy as np

def get_chunks(file_name):

	with open(file_name, 'r') as f:
		# get rid of the first line
		yield [int(i) for i in f.readline().split(',')]

		line = f.readline()
		while line != '':
			chunk = []
			while line not in  ['\n', '']:
				chunk.append([int(i) for i in line.replace('\n', '').split(' ') if i != ''])
				line = f.readline()
			
			if len(chunk) > 0:	
				yield chunk
			line = f.readline()

def play_bingo(values, all_board):
	mask = all_board == print
	for val in values:
		mask = np.logical_or(mask, all_board == val)
		yield mask
	



if __name__ == '__main__':
	# part 1

	chunks_gen = get_chunks('input')

	val_list = next(chunks_gen)

	all_chunks = np.array(list(chunks_gen))

	game = play_bingo(val_list, all_chunks)

	for val, turn in zip(val_list, game):
		check_bingo = np.logical_or(
			np.prod(turn, axis = 1, dtype = bool),
			np.prod(turn, axis = 2, dtype = bool))
		is_winner = np.any(check_bingo, axis = 1)
		if np.any(is_winner):
			winner_grid = all_chunks[is_winner]
			mask = turn[is_winner]

			print('The score of the winning board is :', 
				sum(winner_grid[np.logical_not(mask)]) * val)
			break