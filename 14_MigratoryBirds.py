
birds = [1, 4, 4, 4, 5, 3] # 1 3 4 4 4 5


def migratoryBirds():
    birds1 = [1, 4, 4, 4, 5, 3] # 1 3 4 4 4 5
    return len(birds1)


x = map(migratoryBirds, (1, 4, 4, 4, 5, 3))

print(list(x))



#migratoryBirds(birds)
