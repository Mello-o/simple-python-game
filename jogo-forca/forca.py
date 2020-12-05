def jogar():

	print('\n\n','*'*37)
	print('***** BEM VINDO AO JOGO DA FORCA *****')
	print('*'*38, '\n')
	
	# SETTING THE SECRET WORD
	secret_word = 'banana'

	# SETTING A LIST TO PUT THE USERS'S VALUES
	answer_secret_word = []

	for chances in range(len(secret_word)):
		user_answer = input('Digite uma letra: ')

		if user_answer in secret_word and user_answer not in answer_secret_word:
			for letra in secret_word:
				if letra == user_answer:
					answer_secret_word.append(letra)
					print(f'Parabéns, temos a letra {letra} em {secret_word.count(letra)} posições.')


		elif user_answer in secret_word:
			print('\nVocê já digitou essa letra')

		else:
			print(f'\nA palatra secreta não possui a letra {user_answer}')

	print(answer_secret_word)

if __name__ == '__main__':
	jogar()