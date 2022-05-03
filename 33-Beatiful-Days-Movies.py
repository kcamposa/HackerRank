""""
Lily likes to play games with integers. She has created a new game where she determines the difference between a number and its reverse. 
For instance, given the number 12, its reverse is 21. Their difference is 9. The number 120 reversed is 21, and their difference is 99.

She decides to apply her game to decision making. She will look at a numbered range of days and will only go to a movie on a beautiful day.

Given a range of numbered days,[i...j] and a number K, determine the number of days in the range that are beautiful.
Beautiful numbers are defined as numbers where [i-reverse(i)] is evenly divisible by K. If a day's value is a beautiful number, it is a beautiful day. 
Return the number of beautiful days in the range.

int i: the starting day number
int j: the ending day number
int k: the divisor

"""

def beautifulDays(i, j, k):
    count = 0
    for i in range(i, j+1):
        if ((i - int(str(i)[::-1])) % k) == 0:
            count += 1
    print(count)

if __name__ == '__main__':
    i = 13
    j = 45
    k = 3
    beautifulDays(i, j, k)