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

			if level == 1 or level == 2 or level == 3:
				break
			else:
				print('Ensira um número de 1 a 3, por favor.')

		except ValueError:
			print('Somente números, por favor.')

	letter_word = input('Digite um letra ou palavra (caso vc saiba ;p) : ')	

	# SETTING A LIST TO PUT THE USERS'S VALUES
	users_answer = []

	for letra in secret_word:
		if letra == 





if __name__ == '__main__':
	jogar()