'''
 Given a square matrix, calculate the absolute difference between the sums of its diagonals.
 For example, the square matrix ARR is shown below:
 1 2 3
 4 5 6
 9 8 9
 The left-to-right diagonal = 1+5+9 = 15 and The right to left diagonal = 3+5+9=17. Their absolute difference is 15-17=2.

 three different ways to sum the two diagonal in a two dimensional list
'''
import numpy as np

#----------------------------------------------------------------  1
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
    
#----------------------------------------------------------------  2
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
    
#----------------------------------------------------------------  3
def printDiagonal_3():

    b = [
        [11, 2,  4],
        [4,  5,  6],
        [10, 8, -12]
        ]

    a = [
        [1, 2, 3, 5],
        [4, 5, 6, 7],
        [9, 8, 9, 8],
        [19,77,9,40]
        ]

    long = len(a)
    sumDiagonal_1 = 0
    sumDiagonal_2 = 0
    contador = long-1

    for i in range(long):
        for j in range(len(a[i])):
            if i == j: # first diagonal
                sumDiagonal_1 = sumDiagonal_1 + a[i][j]
            if j == contador: # second diagonal 
                sumDiagonal_2 = sumDiagonal_2 + a[i][j]
                contador += -1
        
    result = abs(sumDiagonal_1-sumDiagonal_2)

    print(result)

printDiagonal_3()
