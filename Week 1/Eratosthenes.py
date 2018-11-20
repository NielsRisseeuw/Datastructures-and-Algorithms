# Naam: Niels Risseeuw
# Studentnummer: 1721586
# Klas: V2C
# Docent: Fritz Dannenberg

def sieveOfEratothenes(maxPrimeNumber):

    assert isinstance(maxPrimeNumber, int), 'Error: Parameter 1 not of type int'
    assert not maxPrimeNumber <= 0, 'Error: Parameter 1 is smaller or equal to zero'

    myList = []

    # Create the list
    for i in range(maxPrimeNumber+1):
        myList.append([i, True])

    #Sieve the prime numbers
    for i in range(2, len(myList)):
        for j in range(len(myList)):
            if i * j > len(myList)-1:
                break
            if not i * j == i:
                myList[i * j][1] = False

    # Remove all non prime numbers
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


print(sieveOfEratothenes(1000))
print(sieveOfEratothenes('c'))
print(sieveOfEratothenes(0))
print(sieveOfEratothenes(1))
