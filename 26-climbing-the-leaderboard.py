

ranked = [100, 90, 90, 80, 75, 60] # scores
player = [50, 65, 77, 90, 102] # alice

def climbingLeaderboard(ranked, player):
    
    positions2 = []

    for score in player:

        positions1=[]
        counter = 0
        deletedNumber = 0

        ranked.append(score)
        ranked = sorted(ranked, reverse=True)

        for num in ranked:

            if len(positions1)==0:
                deletedNumber = num
                counter+=1
                positions1.append(counter)
            else:
                if num == deletedNumber:
                    positions1.append(counter)
                else:
                    deletedNumber = num
                    counter+=1
                    positions1.append(counter)
        
        index = positions1[ranked.index(score)]
        ranked.remove(score)
        positions2.append(index)
    
    print(positions2)



def climbingLeaderboard2(scores, alice):

    scores_set = list(set(scores))
    scores_set.sort(reverse=True)
    result = []
    l = len(scores_set)
    for s in alice:
        aa = scores_set[l-1]
        while (l>0) and (s >= scores_set[l-1]):
            l -= 1
        result.append(l+1)
    print(result)

def climbingLeaderboard3(ranked, player):

    positions = []

    for i in player:

        ranked.append(i)
        ranked = sorted(ranked, reverse=True)
        index = ranked.index(i)

        positions.append(index)
        ranked.remove(i)
    
    print(positions)


climbingLeaderboard3(ranked, player)