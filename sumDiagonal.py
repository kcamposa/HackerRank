import numpy as np

#----------------------------------------------------------------
def printDiagonal_1(): # with numpy
    
    a = [
        [11, 2, 4],
        [4, 5, 6],
        [10, 8, -12]
        ]

    diagonal_1 = np.asarray(a)

    diagonal_2 = np.asarray(a)
    diagonal_2 = np.fliplr(diagonal_2)

    sumDia_1 = np.trace(diagonal_1) # get sum
    sumDia_2 = np.trace(diagonal_2) # get sum

    result = abs(sumDia_1-sumDia_2) # abs of sum

    print("result: ", result) 
#----------------------------------------------------------------    
def printDiagonal_2(): # manual
    a = [
        [11, 2,  4],
        [4,  5,  6],
        [10, 8, -12]
        ]

    diagonal_1 = 0
    diagonal_2 = 0
    n = len(a)-1

    for i in range(len(a)):
        diagonal_1 = diagonal_1 + a[i][i]
                                            
        diagonal_2 = diagonal_2 + a[i][n-i]

    dif = abs(diagonal_1 - diagonal_2)
    
    print(dif)
#----------------------------------------------------------------

def printDiagonal_3():

    a = [
        [11, 2,  4],
        [4,  5,  6],
        [10, 8, -12]
        ]

    b = [
        [1, 2, 3],
        [4, 5, 6],
        [9, 8, 9]
        ]

    long = len(a)
    sumDiagonal_1 = 0
    sumDiagonal_2 = 0
    contador = long-1

    for i in range(long):
        for j in range(len(a[i])):
            if i == j: # first diagonal
                sumDiagonal_1 = sumDiagonal_1 + a[i][j]
            if j == contador:
                sumDiagonal_2 = sumDiagonal_2 + a[i][j]
                contador += -1
        
    result = abs(sumDiagonal_1-sumDiagonal_2)

    print(result)

printDiagonal_3()
