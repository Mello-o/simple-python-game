from random import randint

def secret_word():
	file = open('palavras.txt', 'r')

	words = []

	for lines in file:
		words.append(lines.strip())

	file.close()

	random_number = randint(0, len(words))

	return words[random_number]