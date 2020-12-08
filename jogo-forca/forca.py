import os

def jogar():

	os.system('clear')

	print('\n\n','*'*37)
	print('***** BEM VINDO AO JOGO DA FORCA *****')
	print('*'*38, '\n')
	
	# SETTING THE SECRET WORD
	secret_word = 'banana'.upper()

	print('\nDigite uma letra e tente acertar a palavra secreta a seguir: \n')

	# SETTING A LIST TO PUT THE USERS'S VALUES
	answer_secret_word = ['__', '__', '__', '__', '__','__']

	for chances in range(len(secret_word)):
		
		for letra in answer_secret_word:
			print(letra, end=' ')
		
		while True:
			
			users_answer = input('\n\nDigite uma letra: ').strip().upper()
			index = 0
				
			if users_answer in answer_secret_word:
				print('\nVoce já digitou essa letra...\n')
				break

			elif users_answer not in secret_word:
				print('\nA palavra secreta não possui essa letra...\n')
				break

			else:
				break

		for letra in secret_word:
			
			if letra == users_answer:
				answer_secret_word[index] = letra
			
			index = index + 1



if __name__ == '__main__':
	jogar()

	