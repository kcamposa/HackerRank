import numpy as np
def printDiagonal_1():
    
    a = [
        [11, 2, 4],
        [4, 5, 6],
        [10, 8, -12]
        ]

    diagonal_1 = np.asarray(a)

    diagonal_2 = np.asarray(a)
    diagonal_2 = np.fliplr(diagonal_2)

    sumDia_1 = np.trace(diagonal_1) # suma de la diagonal 1
    sumDia_2 = np.trace(diagonal_2) # suma de la diagonal 2

    result = abs(sumDia_1-sumDia_2)

    print("result: ", result)
    
def printDiagonal_2():
    a = [
        [11, 2,  4],
        [4,  5,  6],
        [10, 8, -12]
        ]

    suma_diagonalprincipal = 0
    suma_diagonalsecundaria = 0
    n = len(a)-1

    for i in range(len(a)):
        suma_diagonalprincipal = suma_diagonalprincipal + a[i][i]
                                            
        suma_diagonalsecundaria = suma_diagonalsecundaria + a[i][n-i]

    dif = abs(suma_diagonalprincipal - suma_diagonalsecundaria)
    
    print(dif)

printDiagonal_2()
    
