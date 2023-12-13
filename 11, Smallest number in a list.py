# This program takes a list of numbers as inputs and finds the smallest.

listOfNumbers = [1,2,3,4,3,5.9,-3.5,6.7,4,2,5,2]
print(min(listOfNumbers))

# Alternative method
listOfNumbers.sort()
print(listOfNumbers[0])

# Another method 
min = listOfNumbers[0]
for anynumber in listOfNumbers:
    if anynumber < min:
        min = anynumber

print(min)