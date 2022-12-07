def run_evolution(population, total_days = 80):
	for _ in range(total_days):
		population['7'] += population['0']
		population = {str(i): population[str((i + 1) % 9)]  for i in range(9)}

	return sum(population.values())

def main(part = 1, test = False):
	if test:
		filename = 'inputtest'
	else:
		filename = 'input'

	if part == 1:
		total_days = 80
	elif part == 2:
		total_days = 256

	with open(filename, 'r') as f:
		line = f.readline()
		population = [int(i) for i in line.split(',')]

	pop = {str(i): population.count(i) for i in range(9)}
	

	print('The total population is : ', run_evolution(pop, total_days = total_days))




if __name__ == '__main__':
	
	#part 1
	main(part = 1)

	#part 2
	main(part = 2)