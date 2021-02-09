# repetitive list, remove repetitive, sorted, find the second sum()
def runnerup():
    arr = [5, 51, 55, 67, 5, 89, 100, 101, 77, 66, 5]
    newList = []

    orderingArr = sorted(arr) # [2, 3, 5, 6, 6]
    print("Sorted: ", orderingArr)


    for n in orderingArr:
        newList.append(n)

    for j in newList: # removing repetitives numbers
        if newList.count(j)>1:
            newList.remove(j)
    
    Ma = max(newList) # find the max number
    newList.remove(Ma)

    Ma_Next = max(newList)
    print("The up-runner score is: ", Ma_Next)        

runnerup()