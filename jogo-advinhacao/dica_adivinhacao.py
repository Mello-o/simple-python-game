def dica_par_impar(tries, number):
	if tries == 5 or tries == 14 or tries == 19:
		num = number % 2
		if num == 1:
			return print('dica... o número é ímpar...')
		else: 
			return print('dica... o número é par...')
			