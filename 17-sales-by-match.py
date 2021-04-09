'''
There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
Example:
n = 7
ar = [1, 2, 1, 2, 1, 3, 2]

There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.
Complete the sockMerchant function in the editor below.
- int n: the number of socks in the pile
- int ar[n]: the colors of each sock

**returns int: the number of pairs
'''

n = 7
ar = [1, 2, 1, 2, 1, 3, 2]
#ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

def sockMerchant(n, ar):

    i = 0
    numbers = []
    countsNumbers = []
    nsPairs = []
    [numbers.append(n) for n in ar if n not in numbers] # getting not repetitives numbers
    #print(numbers)

    for ns in numbers:
        countsNumbers.append(ar.count(ns))

    #print(countsNumbers) # [4, 3, 1, 1]

    for nsP in countsNumbers:
        if nsP > 1 : 
            if nsP%2 != 0:
                nsPairs.append(nsP-1)
            if nsP%2 == 0:
                nsPairs.append(nsP)

    #print(nsPairs) # [4, 2]

    for mun in nsPairs:
        num = mun // 2
        i = i + num

    print(i)

sockMerchant(n, ar)
