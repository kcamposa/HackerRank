# Alice and Bob each created one problem for HackerRank. 
# A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.
# The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]), and the rating for Bob's challenge is the triplet b = (b[0], b[1], b[2]).
# If a[i] > b[i], then Alice is awarded 1 point.
# If a[i] < b[i], then Bob is awarded 1 point.
# If a[i] = b[i], then neither person receives a point.

# Comparate two list at the same time using zip
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
