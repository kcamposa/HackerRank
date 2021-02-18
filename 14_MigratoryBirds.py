
birds = [1, 4, 4, 4, 5, 3] # 1 3 4 4 4 5
#birds = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]

def migratoryBirds_1(arr):

    num = 0
    newList = []

    for i in range(1, 6):
        newList.append(arr.count(i))
    

    
    print(newList)

migratoryBirds_1(birds)