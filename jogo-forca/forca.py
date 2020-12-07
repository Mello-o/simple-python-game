def jogar():

	print('\n\n','*'*37)
	print('***** BEM VINDO AO JOGO DA FORCA *****')
	print('*'*38, '\n')
	
	# SETTING THE SECRET WORD
	secret_word = 'banana'

	print('\nDigite uma letra e tente acertar a palavra secreta a seguir: \n')

	# SETTING A LIST TO PUT THE USERS'S VALUES
	answer_secret_word = ['__', '__', '__', '__', '__','__']

	for chances in range(len(secret_word)):
		
		for letra in answer_secret_word:
			print(letra, end=' ')
		
		while True:
			try:
				users_answer = input('\n\nDigite uma letra: ')
				index = 0
				
				if users_answer in answer_secret_word:
					print('Voce já digitou essa letra...')
				else:
					break
			except ValueError:
				print('Somente letras, por favor.')


		for letra in secret_word:
			
			if letra == users_answer:
				answer_secret_word[index] = letra
			
			index = index + 1



if __name__ == '__main__':
	jogar()

	