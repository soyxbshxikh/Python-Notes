# The [in] keyword in Python is used to check if an item (in this case, the letter) is present.

letter = input("Enter a letter: ")

if letter in 'aeiouAEIOU':
    print("Vowel")
else:
    print("Consonant")
