import random

def autoKeyVigenere(plaintext):
	plaintextList = list()
	for char in plaintext:
		plaintextList.append(ord(char))

	keyPhraseLength = random.randint(0, len(plaintext))
	key = random.sample(xrange(65, 91), keyPhraseLength)
	for codepoint in plaintextList:
		if len(key) < len(plaintext):
			key.append(codepoint)

	cipher = list()
	for x in range (0, len(plaintext)):
		cipher.append((plaintextList[x] + key[x]) % 65 + 65)

	return cipher
