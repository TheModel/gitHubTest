# This program takes in a list of numbers as input and prints all the even numbers

listOfNumbers = [1,2,3,4,5,3,5,3,5,6,7,8,5,10,200]
for anynumber in listOfNumbers:
    if anynumber % 2 == 0:
        print(anynumber, end=" ")

