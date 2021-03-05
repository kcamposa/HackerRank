'''
 Given a chocolate bar, two children, Lily and Ron, are determining how to share it. Each of the squares has an integer on it.
 Lily decides to share a contiguous segment of the bar selected such that:
 -The length of the segment matches Ron's birth month.
 -The sum of the integers on the squares is equal to his birth day.

s = [2,2,1,3,2] --> 4,2
s = [1,1,1,1,1,1] --> 3,2 
s =  [1,2,1,3,2] --> 3,1
'''

s = [4]
d = 4
m = 1

def birthday(squares, d, m): 
    count = 0
    long = len(squares)+1-m
    for i in range(0, len(squares)+1-m): # from 0 to N number of pairs
        if sum(squares[i:i+m]) == d: # sum [start / number : number / End]
            count += 1        
        #print(squares[i:i+m])
    print(count)
    
    #print(len(squares)+1)

birthday(s, d, m)
