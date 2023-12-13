# This program takes a list of numbers as inputs and finds the largest.

listOfNumbers = [1,2,3,4,3,5.9,6.7,4,2,5,2]
print(max(listOfNumbers))

# Alternative method
listOfNumbers.sort()
print(listOfNumbers[len(listOfNumbers) - 1])

# Another method 
max = listOfNumbers[0]
for anynumber in listOfNumbers:
    if anynumber > max:
        max = anynumber

print(max)
