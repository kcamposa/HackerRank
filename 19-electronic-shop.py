'''
A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a give budget. Given price lists for keyboards and USB drives and a budget, find the cost to buy them. 
If it is not possible to buy both items, return -1.

Example:
b = 60
keyboards = [40, 50, 60]
drives = [5, 8, 12]

The person can buy a 40 keyboard + 12 USB drive = 52, or a 50 keyboard + 8 USB drive = 58. Choose the latter as the more expensive option and return 58.
'''

keyboards = [40, 50, 60]
drives = [5, 8, 12]
b = 60


def getMoneySpent(keyboards, drives, b):

    [keyboards.remove(i) for i in keyboards if i >= b]
    [drives.remove(j) for j in drives if j >= b]

    

    #print('hola')


getMoneySpent(keyboards, drives, b)