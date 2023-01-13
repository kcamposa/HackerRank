"""
Another sorting method, the counting sort, does not require comparison. 
Instead, you create an integer array whose index range covers the entire range of values in your array to sort. 
Each time a value occurs in the original array, you increment the counter at that index. 
At the end, run through your counting array, printing the value of each non-zero valued index that number of times.
"""


arr = [1, 1, 3, 2, 1]

def countingSort(arr):
    result = [0]*100
    for i in arr:
        result[i] += 1
    return(result)


if __name__ == '__main__':
    countingSort(arr)