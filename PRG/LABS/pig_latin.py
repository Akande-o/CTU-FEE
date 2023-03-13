word = input("Please enter in a correct word: ")
if word.isalpha():
    word = word.lower()
    pig_word = word[1:] + word[0] + "ay"
print(pig_word)