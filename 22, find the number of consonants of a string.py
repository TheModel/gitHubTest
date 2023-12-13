# This program finds the number of consonants in a string.

string = input("Enter a string: ")
noOfConsonants = 0
for anychar in string:
    if anychar != 'a' and anychar != 'A' and anychar != 'e' and anychar != 'E' and anychar != 'i' and anychar != 'I' and anychar != 'o' and anychar != 'O' and anychar != 'u' and anychar != 'U':
        noOfConsonants += 1
print("The number of vowels in {} is : {}".format(string, noOfConsonants))
