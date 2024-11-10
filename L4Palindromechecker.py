word = input("Please enter a word: ")
letters_in_word = list(word)
letters_in_word.reverse()
reversed_word = "".join(letters_in_word)

if word == reversed_word:
    print(True)
else:
    print(False)
    