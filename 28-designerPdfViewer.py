''''
There is a list of 26 character heights aligned by index to their letters. For example, "a" is at index 0 and "z" is at index 25. There will also be string.
Using the letter heights given, determine the area of the rectangle highlight in mm**2 assuming all letters are 1mm wide.

Example:

    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 1, 1, 5, 5, 1, 5, 2, 5, 5, 5, 5, 5, 5]
word = "torn"

The heights are t=2. o=1, r=1 and n=1. The tallest letter is 2 high and there are 4 letters. The highlighted are will be 2 * 4 = 8 mm**2, so the answer is 8

'''


#     a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
#h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
#word = "abc"

#    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
word = "zaba"
# output 28


def designerPdfViewer(h, word):

    alp = 'abcdefghijklmnopqrstuvwxyz'
    
    nums = []
    for w in word:
        num = alp.index(w) # 19 14 17 13
        nums.append(h[num])

    res = max(nums) * int(len(word))
    print(res) # change for return 

designerPdfViewer(h, word)