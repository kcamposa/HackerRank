'''
A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a give budget. Given price lists for keyboards and USB drives and a budget, find the cost to buy them. 
If it is not possible to buy both items, return -1.

Example:
b = 60
keyboards = [40, 50, 60]
drives = [5, 8, 12]

The person can buy a 40 keyboard + 12 USB drive = 52, or a 50 keyboard + 8 USB drive = 58. Choose the latter as the more expensive option and return 58.
'''

#keyboards = [40, 50, 60]
#drives = [5, 8, 12]
#b = 60
keyboards = [5, 1, 1]
drives = [4]
b = 5

def getMoneySpent(keyboards, drives, b):

    summ = []

    [keyboards.remove(i) for i in keyboards if i >= b] # [40, 50]
    [drives.remove(j) for j in drives if j >= b] # [5, 8, 12]
    
    print('testing')

    for k in keyboards:
        for x in drives:
            if (k+x) <= b:
                summ.append(k + x)

    if not summ:
        print(-1)
    else:
        print(max(summ))

getMoneySpent(keyboards, drives, b)