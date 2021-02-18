
birds = [1, 4, 4, 4, 5, 3] # 1 3 4 4 4 5


def migratoryBirds(arr):
    
    NewList = []
    newBirds = birds
    


    #for j in newBirds:
    #    if newBirds.count(j)>1:
    #        newBirds.remove(j)

    #print(newBirds)

    #for position in range(0, len(newBirds)):
    for position in range(0, len(arr)):
        count = 0
        for j in arr:
            if j in arr:
                count += 1

        NewList.insert(arr[position], count)
        
    print(NewList)

migratoryBirds(birds)
