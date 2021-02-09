def find():
    arr = [1, 2, 3, 4, 5]

    sumWithMax = 0
    sumWithMin = 0

    num = False
    count = 0

    for i in arr: # true o false, if the list has the same value in the positions.
        if i == arr[0]:
            count += 1
        if count == len(arr):
            num = True


    if num == False:
        for i in arr:
            maxNumber = max(arr)
            minNumber = min(arr)

            if i != maxNumber:
                sumWithMin += i
            
            if i != minNumber:
                sumWithMax += i
    else: # if the list has the same value in all boxes
        maxNumber = arr[0]
        arr.remove(maxNumber)
        
        sumWithMin = sum(arr)
        sumWithMax = sum(arr)


    print(sumWithMin, sumWithMax)



find()