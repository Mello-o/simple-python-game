import random
import dica_adivinhacao
import os

def jogar():

	os.system('cls' if os.name == 'nt' else 'clear')

	print('\n*'*5)
	print('****** BEM VINDO AO JOGO DE ADIVINHAÇÃO ******')

	print('\n\nEscolha o seu nível: ')
	print(
	'''(1) Fácil - 20 tentativas
	(2) Médio - 10 tentivas
	(3) Difícil - 5 tentivas''')


	while True:
		try:
			level = int(input('Digite o nível: '))
			
			if level == 1 or level == 2 or level == 3:
				break
			else:
				print('Ensira um número entre 1 e 3, por favor.')

		except ValueError:
			print('Ensira um número, por favor.')


	# SETTING CHANCES BY THE LEVEL
	if level == 1: 
		tries = 20

	elif level == 2:
		tries = 10

	else:
		tries = 5


	# RANDOM NUMBER
	number_random = random.randint(0, 101)



	print('\n\nAdivinhe um número entre 0 e 100!\n\n')


	for chances in range(0, tries):
		
		while True:
			try:
				print(f'Tentativa {chances + 1} de {tries}')
				user_number = int(input('Tente adivinhar.. qual é o número? '))
				break
			except ValueError:
				print('Apenas números por favor...')

		higher = user_number < number_random
		lower = user_number > number_random
			
		if higher:
			print('\nO número é maior...\n')
			dica_adivinhacao.dica_par_impar(chances, number_random)
		elif lower:
			print('\nO número é menor...\n')
			dica_adivinhacao.dica_par_impar(chances, number_random)
		else:
			print('\nVOCE ACERTOU!\n')
			break

	if user_number != number_random:
		print('Infelizmente voce não acertou. O número era ', number_random)

if __name__ == '__main__':
	jogar()
