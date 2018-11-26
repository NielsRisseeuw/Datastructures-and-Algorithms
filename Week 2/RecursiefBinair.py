# Naam: Niels Risseeuw
# Studentnummer: 1721586
# Klas: V2C

def MyBinair(Data):
    assert Data >= 0, 'Error: Parameter 1 is not allowed to be negative'
    assert isinstance(Data, int), 'Error: Parameter 1 is required int'

    if Data == 0:
        return str(0)
    if Data == 1:
        return str(1)
    else:
        return str(MyBinair(int(Data/2))) + str(Data%2)


print(MyBinair(100))

