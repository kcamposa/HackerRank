def find():
    arr = [1, 3, 5, 7, 9]

    sumWithMax = 0
    sumWithMin = 0

    for i in arr:
        maxNumber = max(arr)
        minNumber = min(arr)

        if i != maxNumber:
            sumWithMin += i
        
        if i != minNumber:
            sumWithMax += i
            
    print(sumWithMin, sumWithMax)


find()