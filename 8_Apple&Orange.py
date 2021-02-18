# Sam's house has an apple tree and an orange tree that yield an abundance of fruit. 
# Using the information given below, determine the number of apples and oranges that land on Sam's house.

# -The red region denotes the house, where S is the start point, and T is the endpoint. 
# The apple tree is to the left of the house, and the orange tree is to its right.

# -Assume the trees are located on a single point, where the apple tree is at point A, and the orange tree is at point B.
# -When a fruit falls from its tree, it lands D units of distance from its tree of origin along the X-axis. *A negative value of D means the fruit fell D units to the tree's left, 
# and a positive value of D means it falls D units to the tree's right.

def Apple_Orange():
    s = 7 # starting point of sam's house 
    t = 10 # ending location of sam's house

    a = 4 # apple tree
    b = 12 # orange tree

    apples = [2, 3, -4]
    oranges = [3, -2, -4]

    newApples = []
    newOranges = []

    rangeFruits = []
    countApples = 0
    countOranges = 0

    for apple in apples:
        newApples.append(a + apple) # [6, 7, 0] = 1

    for orange in oranges:
        newOranges.append(b + orange) # [15, 10, 8] = 2
    
    for i in range(s, t+1):
        rangeFruits.append(i) # [7, 8, 9, 10]

    for newApple in newApples:
        if newApple in rangeFruits:
            countApples += 1 
    
    for newOrange in newOranges:
        if newOrange in rangeFruits:
            countOranges += 1

    print(countApples)
    print(countOranges)


def Apple_Orange_1():

    s = 7 # starting point of sam's house 
    t = 10 # ending location of sam's house

    a = 4 # apple tree
    b = 12 # orange tree

    apples = [2, 3, -4]
    oranges = [3, -2, -4]

    print(sum([1 for x in apples if (x + a) >= s and (x + a) <= t]))
    print(sum([1 for x in oranges if (x + b) >= s and (x + b) <= t]))
