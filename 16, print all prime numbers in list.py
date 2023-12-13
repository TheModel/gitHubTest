# This program takes in a list of numbers and prints all the prime numbers in the list.

listOfNumbers = [1,2,3,4,5,6,7,8,9,10,11,12,14,16, 57, 23]

for anynumber in listOfNumbers:
    noOfFactors = 0
    for i in range(1, anynumber + 1):
        if anynumber % i == 0:
            noOfFactors += 1
    if noOfFactors == 2:
            print(anynumber)
