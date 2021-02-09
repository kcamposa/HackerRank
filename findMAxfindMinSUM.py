#Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
#Then print the respective minimum and maximum values as a single line of two space-separated long integers.
# Example: arr = [1, 3, 5, 7, 9], The minimum sum is 1+3+5+7 = 15 and the maximum sum is 3+5+7+9=24, The function prints: 16  24

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
