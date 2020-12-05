def jogar():

	print('\n*'*10)
	print('***** BEM VINDO AO JOGO DA FORCA *****')
	print('*'*10, '\n')
	
	# SETTING THE SECRET WORD
	secret_word = 'banana'

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