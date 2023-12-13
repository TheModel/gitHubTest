# This program finds the number of vowels in a string.

string = input("Enter a string: ")
NoOfVowels = 0
for anychar in string:
    if anychar == 'a' or anychar == 'A' or anychar == 'e' or anychar == 'E' or anychar == 'i' or anychar == 'I' or anychar == 'o' or anychar == 'O' or anychar == 'u' or anychar == 'U':
        NoOfVowels += 1
print("The number of vowels in {} is : {}".format(string, NoOfVowels))
