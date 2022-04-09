
word = "aaabccc"

def sizeOfSubstring(word):
    wd = []
    for i in word: # aaabccc
        w  = word.count(i) # how many numbers 
        if w > 1:
            if i not in wd:
                wd.append(i) 
        else:
            wd.append(i)
    s = ''.join([str(l) for l in wd]) # convert array to string
    print(s) # abc

sizeOfSubstring(word)