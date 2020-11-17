def primesInList(myList):
    z = list()
    for x in myList:
        if (x <= 1):
            y = False
        else:
            for i in range(2, x//2):
                if (x % i) == 0:
                    y = False
                else:
                    y = True
        if (y == True):
            z.append(i)
    return(z)

def primesInList(myList):
    z = list()
    for num in myList:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                z.append(num)
    return(z)