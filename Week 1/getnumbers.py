def getNumbers(s):
    assert isinstance(s, str), 'Error: Parameter s is not a string'

    myList = []
    Temp = s[0]
    stringNumber = 0

    for i in range(0, len(s)):
        if s[i].isdigit():
            stringNumber *= 10
            stringNumber += int(s[i])

        if i == len(s)-1:
            Temp = s[i]

        if Temp.isdigit() and (not s[i].isdigit() or i == len(s)-1):
            myList.append(stringNumber)
            stringNumber = 0

        Temp = s[i]

    return myList

myString = 'een123zin45 6met-632meerdere+7777getallen'

print(getNumbers(myString))

