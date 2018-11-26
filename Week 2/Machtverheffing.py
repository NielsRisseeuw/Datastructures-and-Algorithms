# Naam: Niels Risseeuw
# Studentnummer: 1721586
# Klas: V2C

def machtv3(a, n):
    assert n > 0, 'Error, Parameter n needs to be larger than 0'

    m = 1
    while n > 0:
        if n%2 == 0:
            n /= 2
            a = a * a

        else:
            n = n - 1
            m = m * a

    return m

# Output: 78125
print(machtv3(5, 7))
