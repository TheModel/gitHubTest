# This program takes in a list of numbers as input and prints all the odd numbers

listOfNumbers = [1,2,3,4,5,6,7,8,10,200, 45]
for anynumber in listOfNumbers:
    if anynumber % 2 == 1:
        print(anynumber, end=" ")