# This program checks if a string is palindrome

def IsStringPalindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

string = input("Enter a string: ")
print("Is {} palindrome? answer = {}".format(string, IsStringPalindrome(string)))



