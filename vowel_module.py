def vowel_counting(name):
    vowels = "AEIOUaeiou"
    count = 0
    for letter in name:
        if letter in vowels:
            count += 1
    print(f"My full name is {name}.")
    print(f"I have {count} vowels in my name.")