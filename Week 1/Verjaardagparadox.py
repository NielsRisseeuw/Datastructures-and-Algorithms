import random

# Generates list containing 100 lists of 23 randomly generated numbers
def VerjaardagParadox(TestQuantity, GroupSize):

    assert isinstance(TestQuantity, int), 'Error: Parameter 1 is not of type int'
    assert isinstance(GroupSize, int), 'Error: Parameter 2 is not of type int'
    assert not TestQuantity <= 0, 'Error: Parameter 1 cannot be of length 0 or smaller'
    assert not GroupSize <= 0, 'Error: Parameter 2 cannot be of length 0 or smaller'

    CheckList = []
    ConstList = []
    MyList = []

    DoubleBirthdays = 0
    TempInt = 0

    # Creates list of 365 days long filled with false
    for i in range(0, 365):
        ConstList.append(False)

    # Copies ConstList into Checklist
    CheckList = list(ConstList)

    for i in range(TestQuantity):

        # Picks [GroupSize] times random int and checks if has already been randomly selected, breaks if duplicate is found
        for j in range(GroupSize):
            TempInt = random.randint(0, 364)
            if CheckList[TempInt]:
                DoubleBirthdays += 1
                break

            CheckList[TempInt] = True
            MyList.append(TempInt)
        MyList = []
        CheckList = list(ConstList)

    # Return percentage in float
    return DoubleBirthdays/TestQuantity * 100

print(VerjaardagParadox(100, 23))
print(VerjaardagParadox(-1, 23))
print(VerjaardagParadox(100, -1))
print(VerjaardagParadox('test', 23))
print(VerjaardagParadox(100, 'test'))
