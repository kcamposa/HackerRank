# Given an array of bird sightings where every element represents a bird type id, determine the id # of the most frequently sighted type. If more than 1 type has been spotted that maximum amount, # # return the smallest of their ids.




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
            for k in range(5):
                if newList[k] == max_:
                    print(k+1)
    else: # only max 1
        for i in range(5):
            if newList[i] == max_:
                print(i+1)

    

migratoryBirds_1(birds)

def migratoryBirds_1(arr):
    l = [arr.count(i) for i in range(1, 6)]
    print(l)
    for i in range(len(l)):
        if l[i]==max(l):
            print(i+1)

migratoryBirds_1(birds)