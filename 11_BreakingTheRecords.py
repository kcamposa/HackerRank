'''
 Maria plays college basketball and wants to go pro. 
 Each season she maintains a record of her play. 
 She tabulates the number of times she breaks her season record for most points and least points in a game. 
 Points scored in the first game establish her record for the season, and she begins counting from there.

 For example, assume her scores for the season are represented in the array scores=[12,24,10,24]. 
 Scores are in the same order as the games played. She would tabulate her results as follows:

                                 Count
Game  Score  Minimum  Maximum   Min Max
 0      12     12       12       0   0
 1      24     12       24       0   1
 2      10     10       24       1   1
 3      24     10       24       1   1

 Given the scores for a season, find and print the number of times Maria breaks her records for most and least points scored during the season.
 
'''

scores = [10, 5, 20, 20, 4, 5, 2, 25, 1] # 2 4

scores1 = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42] # 4 0

def breakingRecords(scores_):

    min = max = scores_[0]    
    min_count = max_count = 0

    for i in scores_:
        if i > max:
            max_count += 1
            max = i
        if i < min:
            min_count += 1
            min = i
            
    print(max_count, min_count)

breakingRecords(scores)
