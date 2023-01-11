"""
Given an array of integers, where all elements but one occur twice, find the unique element.
"""

a = [1, 2, 3, 4, 3, 2, 1]

def lonelyinteger(a):
    # Write your code here
    for integer in a:
        if a.count(integer) == 1:
            print(integer)
            return integer
            


if __name__ == '__main__':
    lonelyinteger(a)