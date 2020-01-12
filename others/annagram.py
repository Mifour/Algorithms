"""
annagram: for a sentence composed of strings, returned every couple of word that are annagram to each other
O(n) time & space
"""
def annagram(sentence):
	words = sentence.split()
	dico = {}
	reversed_dico = {}

	for word in words:
		letters = "".join(sorted(list(word)))
		reversed_dico[letters] = reversed_dico[letters] + [word] if letters in reversed_dico else [word]

	res = []
	for value in reversed_dico.values():
		if len(value) > 1:
			res.append(value)

	return res

print(annagram(
		"le chien marche vers sa niche et trouve une limace de chine nue pleine de malicequi lui fait du charme"
	))
print("answer:")
print("[une, nue], [marche, charme], [chien, chine, niche], [malice, limace]")