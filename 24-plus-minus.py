
arr = [-4, 3, -9, 0, 4, 1]

def plusMinus(arr):

    positive = 0
    negative = 0
    zero = 0

    for i in arr:
        if i > 0:
            positive += 1
        if i < 0:
            negative += 1
        if i == 0:
            zero += 1

    p = positive / len(arr)
    n = negative / len(arr)
    z = zero / len(arr)

    print(float("{:.6}".format(p)))
    print(float("{:.6}".format(n)))
    print(float("{:.6}".format(z)))


plusMinus(arr)