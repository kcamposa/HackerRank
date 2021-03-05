'''
 create a stairs with 'count +' and 'count -'

             #
            ##
          ####
         #####
        ######
'''
def printStairs(n):
    countUp = 1
    countDown = n-1

    while(countUp <= n): 
        if countUp == n:
            print(("#" * countUp))
            countUp += 1
            countDown += -1
        else:
            print((" " * countDown) + ("#" * countUp))
            countUp += 1
            countDown += -1

printStairs(6)
