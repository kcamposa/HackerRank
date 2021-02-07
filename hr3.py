def runnerup():
    arr = [2, 3, 5, 80, 6, 71, 6, 9, 9, 66, 66, 67, 100]
    newList = []

    orderingArr = sorted(arr) # [2, 3, 5, 6, 6]
    print("Sorted: ", orderingArr)


    for n in orderingArr:
        newList.append(n)

    for j in newList:
        if newList.count(j)>1:
            newList.remove(j)
    
    Ma = max(newList)
    newList.remove(Ma)

    Ma_Next = max(newList)
    print("The up-runner score is: ", Ma_Next)        

runnerup()