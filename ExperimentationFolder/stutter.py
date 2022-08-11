
word=input("Word?")
def stutter(word):
	return f'{word[0:2]}... {word[0:2]}... {word}?'

print(stutter(word))

