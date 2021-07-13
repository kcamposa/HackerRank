'''
There is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. 
The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2.
The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. It is always possible to win the game.

Example:
c = [0,1,0,0,0,1,0]
'''


def jumpingOnClouds(c): # list
    if len(c) == 1 : return 0

    if len(c) == 2: return 0 if c[1]==1 else 1

    if c[2]==1: return 1 + jumpingOnClouds(c[1:])

    if c[2]==0: return 1 + jumpingOnClouds(c[2:])
