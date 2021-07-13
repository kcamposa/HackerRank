

a = [1, 2, 2, 3, 1, 2]

def pickingNumbers(a):

    maximum=0
    for i in a:
        c = a.count(i) # how many times is I in array
        d = a.count(i-1) # how many times is I-1 in array
        c = c + d
        if c > maximum:
            maximum=c
    print(maximum)

pickingNumbers(a)