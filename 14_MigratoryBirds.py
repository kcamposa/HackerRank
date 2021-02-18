
#birds = [1, 4, 4, 4, 5, 3] # 1 3 4 4 4 5
birds = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]

def migratoryBirds_1(arr):

    newList = []

    for i in range(1, 6):
        newList.append(arr.count(i))

    print(newList)
    
    max_ = max(newList)

    if arr.count(max_)>1:
        if arr.count(max_)==5: # numbers same amount
            print(arr[0])
        else:
            pass
    else: # only max 1
        for i in range(5):
            if newList[i] == max_:
                print(i+1)

    

migratoryBirds_1(birds)