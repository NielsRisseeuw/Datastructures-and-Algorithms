# Naam: Niels Risseeuw
# Studentnummer: 1721586
# Klas: V2C

counter = 0

import random

def swap(a,i,j):
    a[i],a[j] = a[j],a[i]


def qsortNormal(a,low=0,high=-1):
    global counter
    if high == -1:
        high = len(a) -1
    if low < high:
        swap(a,low, random.randint(low,high))
        m = low
        for j in range(low+1,high+1):
            counter += 1
            if a[j] < a[low]:
                m += 1
                swap(a,m,j)
        # low < i <= m : a[i] < a[low]
        # i > m : a[i] >= a[low]
        swap(a,low,m)
        # low <= i < m : a[i] < a[m]
        # i > m : a[i] >= a[m]
        if m > 0:
            qsortNormal(a,low,m-1)
        qsortNormal(a,m+1,high)

def quickWorstSortNormal(a,low=0,high=-1):
    global counter
    if high == -1:
        high = len(a) -1
    if low < high:
        swap(a,low, a.index(min(a[low:high])))
        m = low
        for j in range(low+1,high+1):
            counter += 1
            if a[j] < a[low]:
                m += 1
                swap(a,m,j)
        # low < i <= m : a[i] < a[low]
        # i > m : a[i] >= a[low]
        swap(a,low,m)
        # low <= i < m : a[i] < a[m]
        # i > m : a[i] >= a[m]
        if m > 0:
            qsortNormal(a,low,m-1)
        qsortNormal(a,m+1,high)

# Quicksort normaal                     (Ongeveer 150000-160000)
MyList = random.sample(range(10000), 10000)
qsortNormal(MyList, counter)
print(counter)

MyList = random.sample(range(10000), 10000)
counter = 0
# Quicksort met worst case pivots       (Ongeveer 20000 groter per iteratie van Quicksort)
quickWorstSortNormal(MyList, counter)
print(counter)


