def oddNumbers(l, r):
    myOddArray = []
    for num in range (l, r + 1):
        if num % 2 != 0:
            myOddArray.append(num)
    return myOddArray
