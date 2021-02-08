# comparate two list at the same time using zip
def AliceANDBob():
    a = [5, 6, 7]
    b = [3, 6, 10]

    aliScore = 0
    BobScore = 0

    for al,bo in zip(a,b):
        if al > bo:
           aliScore += 1
        if al < bo:
            BobScore += 1
    
    print(aliScore, BobScore)


AliceANDBob()