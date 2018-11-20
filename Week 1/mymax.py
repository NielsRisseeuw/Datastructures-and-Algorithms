def mymax(a):

    assert len(a) != 0, "Error: List length cannot be 0!"

    # Checks each index if it is bigger than MaxNumber, if it is. MaxNumber = i and continues
    MaxNumber = a[0]
    for i in a:
        assert isinstance(i, (int, float)), "Error, non digit variable in MyList"
        if i > MaxNumber:
            MaxNumber = i
    return MaxNumber

MyList = [1, 2, 5.5, 3, 4]

print(mymax(MyList))
