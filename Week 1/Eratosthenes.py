def sieveOfEratothenes(myList):
    assert isinstance(myList, list), 'Error: Parameter 1 not of type List'

    for i in range(2, len(myList)):
        for j in range(len(myList)):
            if i * j > len(myList)-1:
                break
            if not i * j == i:
                myList[i * j][1] = False
    return myList


def deleteNonPrimes(myList):

    tempList = []

    for i in range(len(myList)):
        if myList[i][1]:
            tempList.append(i)
    return tempList


def createList(Size):

    myList = []

    for i in range(Size+1):
        myList.append([i, True])
    return myList


primeList = createList(100000)
primeList = sieveOfEratothenes(primeList)
primeList = deleteNonPrimes(primeList)
print(primeList)
