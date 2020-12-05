def jogar():

	print('\n*'*10)
	print('***** BEM VINDO AO JOGO DA FORCA *****')
	print('*'*10, '\n')
	
	# SETTING THE SECRET WORD
	secret_word = 'banana'

	# MENU OF TRIES
	print('''Menu de Tentativas
	(1) Fácil - 20 tentativas
	(2) Médio - 10 tentativas
	(3) Difícil - 5 tentivas''')
	
	while True:
		try:
			level = int(input('digite o nível do jogo: '))

			if level == 1:
				level = 20
				break

			elif level == 2:
				level = 15
				break

			elif level == 3:
				level = 5	
				break

			else:
				print('Ensira um número de 1 a 3, por favor.')

		except ValueError:
			print('Somente números, por favor.')


	# SETTING A LIST TO PUT THE USERS'S VALUES
	answer_secret_word = []

	for chances in range(level):
		user_answer = input('Digite uma letra: ')

		if user_answer in secret_word and user_answer not in answer_secret_word:
			for letra in secret_word:
				if letra == user_answer:
					answer_secret_word.append(letra)
		else:
			print('Não tem essa letra na palavra.')

	print(answer_secret_word)

if __name__ == '__main__':
	jogar()