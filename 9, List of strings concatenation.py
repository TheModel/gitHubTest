# This program takes a list of strings as inputs and concatenates them.

listOfNames = ["Ngoh", "Maximus", "Ayisih", "The", "Model", "12"]
concatenatedString = ""
for anyname in listOfNames:
     concatenatedString = concatenatedString + " " + anyname
     # OR 
     # concatenatedString += anyname

print(concatenatedString)
