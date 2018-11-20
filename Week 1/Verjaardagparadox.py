import random

# Generates list containing 100 lists of 23 randomly generated numbers
def VerjaardagParadox(TestQuantity, GroupSize):

    CheckList = []
    ConstList = []
    MyList = []

    DoubleBirthdays = 0
    TempInt = 0

    for i in range(0, 365):
        ConstList.append(False)

    CheckList = list(ConstList)

    for i in range(TestQuantity):

        for j in range(GroupSize):
            TempInt = random.randint(0, 364)
            if CheckList[TempInt]:
                DoubleBirthdays += 1
                break

            CheckList[TempInt] = True
            MyList.append(TempInt)
        MyList = []
        CheckList = list(ConstList)

    return DoubleBirthdays/TestQuantity * 100


TotalDuplicates = VerjaardagParadox(100, 23)
print(TotalDuplicates)
