
k = 7
height = [2, 5, 4, 5, 2]

def hurdleRace(k, height):
    
    maxi = max(height)
    if maxi > k:
        doses = maxi - k
        print(doses)
    else:
        print(0)

hurdleRace(k, height)