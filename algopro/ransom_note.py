def ransom_note(note, magazine):
	histo_note = {0 for l in ["abcdefghijklmnopqrstuvwxyz"]}
	histo_magazine = {0 for l in ["abcdefghijklmnopqrstuvwxyz"]}
	for letter in list(note):
		histo_note[letter] +=1
	for letter in list(magazine):
		histo_magazine[letter] +=1

	for letter in histo_note:
		if not letter in histo_magazine or histo_note[letter] > histo_magazine[letter]:
			return False
	return True