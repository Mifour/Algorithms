def caesarCipherEncryptor(string, key):
	res  = []
	for letter in string:
		res.append(chr((ord(letter)-97+key)%26+97))
	return ''.join(res)
