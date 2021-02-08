def printStairs(n):
    countUp = 1
    countDown = n

    while(countUp <= n):
        
        print((" " * countDown) + ("#" * countUp))
        countUp += 1
        countDown += -1

printStairs(6)