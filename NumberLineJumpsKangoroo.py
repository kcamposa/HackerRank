# You are choreographing a circus show with various animals. 
# For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

# The first kangaroo starts at location X1 and moves at a rate of V1 meters per jump.
# The second kangaroo starts at location X2 and moves at a rate of V2 meters per jump.

# You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. 
# If it is possible, return YES, otherwise return NO.

# Example: Kangaroo 1 starts at X1 = 2 with a jump distance V1 = 1 and kangaroo 2 starts at X2 = 1 with a jump distance
# of V2 = 2. After one jump, they are both at X=3, (X1+V1=2+1, X2+V2=1+2), so the answer is YES.


# x1, v1 = starting position and jump distance for kangaroo 1
# x2, v2 = starting position and jump distance for kangaroo 2

# 28 8 96 2 --> NO
# 43 5 49 3 --> YES
# 21 6 47 3 --> NO 

def NumberLineJumps(x1, v1, x2, v2):

    option = "NO"
    if (x2 - x1) * (v2 - v1) < 0 and (x2 - x1) % (v2 - v1) == 0:
        option = "YES"
    
    return option




def NumberLineJumps_1(x1, v1, x2, v2): # completed

    print("YES" if (x2 - x1) * (v2 - v1) < 0 and (x2 - x1) % (v2 - v1) == 0 else "NO")

    #print((x2 - x1),'%', (v2 - v1),'=', (x2 - x1)%(v2 - v1))

NumberLineJumps(43,5,49,3)