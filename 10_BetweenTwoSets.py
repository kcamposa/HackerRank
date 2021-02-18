# There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

# 1. The elements of the first array are all factors of the integer being considered
# 2. The integer being considered is a factor of all elements of the second array
# These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

# Example: 
# a = [2,6]
# b = [24, 36]
# There are two numbers between the arrays: 6 and 12.
# 6%2=0, 6%6=0, 24%6=0, 36%6=0 for the first value.
# 12%2=0, 12%6=0 and 24%12=0, 36%12=0 for the second value. Return 2.
# resume
# 1. find the LCM of all the integers of array A.
# 2. find the GCD of all the integers of array B.
# 3. Count the number of multiples of LCM that evenly divides the GCD.

a = [2, 6]
b = [24, 36]

def getTotalX(a, b):

    maxA = max(a)
    minB = min(b)
    count = 0
    for i in range(maxA, minB+1):
        if all([i%j==0 for j in a]):
            if all([j%i==0 for j in b]):
                count += 1
    print(count)

getTotalX(a, b)
