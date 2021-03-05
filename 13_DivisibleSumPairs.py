'''
 Given an array of integers and a positive integer K, determine the number of (i, j) pairs where I<J
 and AR[i]+ar[j] is divisible by K.
 ar=[1,2,3,4,5,6]
 k=5
 three pairs meet in: [1,4], [2,3] and [4,6]

ar = [1, 2, 3, 4, 5, 6]
k = 5
n = 6
'''
ar = [1, 3, 2, 6, 1, 2]
n = 6
k = 3


def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(0, n):
        for j in range(i+1, n):
            #num1 = ar[i] 
            #num2 = ar[j] 
            if (ar[i] + ar[j]) % k == 0:
                count += 1
    print(count)

divisibleSumPairs(n, k, ar)
