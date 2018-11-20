def getNumbers(s):
    assert isinstance(s, str), 'Error: Parameter s is not a string'
    assert not len(s) == 0, 'Error: Parameter S is of length zero'

    myList = []
    Temp = s[0]
    stringNumber = 0

    # Loop
    for i in range(0, len(s)):

        # Checks if is a digit, if multiplies by 10
        if s[i].isdigit():
            stringNumber *= 10
            stringNumber += int(s[i])

        # Checks if at end of string, if true sets temp = i to catch last integers at end of string
        if i == len(s)-1:
            Temp = s[i]

        # Checks if i-1 is an int, and if i is int or if at end of sentence
        if Temp.isdigit() and (not s[i].isdigit() or i == len(s)-1):
            myList.append(stringNumber)
            stringNumber = 0

        Temp = s[i]

    return myList

myString = 'een123zin45 6met-632meerdere+7777getallen'
myFaultyString = ''
magicNumber = 1

print(getNumbers(myString))
print(getNumbers(myFaultyString))
print(getNumbers(magicNumber))

