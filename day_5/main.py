import numpy as np
import itertools as itt

def is_in_diagonal(x3, y3, x1, y1, x2, y2):
	is_diagonal = abs(x1 - x2) == abs(y1 - y2)
	is_pos_aligned = (y1 - y2) * (x1 - x3) - (y1 - y3) * (x1 - x2) == 0
	is_inside = (
		(x3 - min(x1, x2) >= 0) and (x3 - max(x1, x2) <= 0)
		and (y3 - min(y1, y2) >= 0) and (y3 - max(y1, y2) <= 0))

	return is_diagonal and is_inside and is_pos_aligned 

def parse_line(line):
	coordinates = line.replace('\n', '').split(' -> ')
	coordinates = [numbers.split(',') for numbers in coordinates]
	coordinates = [[int(i) for i in coords] for coords in coordinates]
	return coordinates

def build_field_danger(filename, part = 1):

	edges = (1, 1)
	field = np.zeros(edges)

	with open(filename, 'r') as f:
		for line in f:
			coords = parse_line(line)
			start_x, start_y = coords[0]
			stop_x, stop_y = coords[1]
			old_edges = edges
			edges = (
				max(start_x + 1 , stop_x + 1, edges[0]),
				max(stop_x + 1, stop_y + 1, edges[1]))
			max_dim = max(edges)
			edges = (max_dim, max_dim)
			if edges != field.shape:
				new_field = np.zeros(edges)
				new_field[:(old_edges[0]), :(old_edges[1])] = field
				field = new_field
				I = np.repeat(range(edges[0]), repeats = edges[1]).reshape(edges)
				J = np.transpose(I)

			low_x, high_x = min(start_x, stop_x), max(start_x, stop_x) + 1
			low_y, high_y = min(start_y, stop_y), max(start_y, stop_y) + 1
			
			if (start_x == stop_x) or (start_y == stop_y):
				field[low_x:high_x, low_y:high_y] += 1
			elif part == 2 and (abs(start_x - stop_x) == abs(start_y - stop_y)):
				mask_diag = (I - stop_x) * (start_y - stop_y) == (J - stop_y) * (start_x - stop_x)
				mask_between = (
					np.logical_and(
						np.logical_and(
							np.greater_equal(high_x - 1, I),
							np.greater_equal(I, low_x)),
						np.logical_and(
							np.greater_equal(high_y - 1, J),
							np.greater_equal(J, low_y)))
					)
				field[np.logical_and(mask_diag, mask_between)] += 1

			yield field

if __name__ == '__main__':
	# part 1
	field_gen = build_field_danger('input')
	for field in field_gen:
		pass
	print('There is at least', np.sum(field >= 2), 'points with at least two lines overlapping',
		'considering only horizontal or vertical vents')

	# part 2
	field_gen = build_field_danger('input', part = 2)
	for field in field_gen:
		pass
	print('There is at least', np.sum(field >= 2), 'points with at least two lines overlapping',
		'considering vertical, horizontal and diagonal vents')