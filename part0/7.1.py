text = input('Enter your text: ')
word_list = sorted(text.split(), key=len)

print("Max len:", len(word_list[::-1][0]))
