word = input("Please enter a word to check if it's a palindrome: ")
word = word.lower()

if word == word[::-1]:
    print(True)
else:
    print(False)