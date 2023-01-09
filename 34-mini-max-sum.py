"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated long integers.

"""

arr = [1, 3, 5, 7, 9]
arr2 = [1, 2, 3, 4, 5]
arr3 = [7, 69, 2, 221, 8974]

def miniMaxSum(arr):
    nArr = sorted(arr)
    print(sum(nArr[:4]), sum(nArr[-4:]))

miniMaxSum(arr3)