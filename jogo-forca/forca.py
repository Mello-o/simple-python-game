import os
import selecao_palavra

def jogar():

	os.system('clear')

	print('\n\n','*'*37)
	print('***** BEM VINDO AO JOGO DA FORCA *****')
	print('*'*38, '\n')
	
	# SETTING THE SECRET WORD
	secret_word = selecao_palavra.secret_word().upper()

	print('\nDigite uma letra e tente acertar a palavra secreta a seguir: \n')

	# SETTING A LIST TO PUT THE USERS'S VALUES
	correct_letters = ['__' for letra in secret_word]


	for chances in range(len(secret_word)):
		
		for letra in correct_letters:
				print(letra, end = ' ')
		
		while True:
			
			users_answer = input('\n\nDigite uma letra: ').strip().upper()
			index = 0
				
			if users_answer in correct_letters:
				print('\nVoce já digitou essa letra...\n')
				break

			elif users_answer not in secret_word:
				print('\nA palavra secreta não possui essa letra...\n')
				break

			else:
				break

		for letra in secret_word:
			
			if letra == users_answer:
				correct_letters[index] = letra
			
			index = index + 1

		if '__' not in correct_letters:
			print('-'*48)
			print('\n###  VOCÊ ACERTOU A PALABRA SECRETA!!!  ###')
			print('\n  *****', secret_word, '*****  \n')
			print('-'*48)
			break

	print('\n\nFim do jogo...\n')

if __name__ == '__main__':
	jogar()

	