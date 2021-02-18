
birds = [1, 4, 4, 4, 5, 3] # 1 3 4 4 4 5
#birds = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
newList = []

def migratoryBirds_1(arr):

    

    for i in range(1, 6):
        newList.append(arr.count(i))

    print(newList)
    
    max_ = max(newList)

    if arr.count(max_)>1:
        pass
    else:
        index = SearchMax(max_)
        print(index)

def SearchMax(number):

    for i in range(5):
        num = newList[i]
        if newList[i] == number:
            return i+1

    

migratoryBirds_1(birds)