'''
Two cats and a mouse are at various positions on a line. You will be given their starting positions. 
Your task is to determine which cat will reach the mouse first, assuming the mouse does not move and the cats travel at equal speed. 
If the cats arrive at the same time, the mouse will be allowed to move and it will escape while they fight.

You are given Q queries in the form of x, y and z representing the respective positions for cats A and B, and for mouse C.
Complete the function catAndMouse to return the appropriate answer to each query, which will be printed on a new line.

- If cat A catches the mouse first, print Cat A.
- If cat B catches the mouse first, print Cat B.
- If both cats reach the mouse at the same time, print Mouse C as the two cats fight and mouse escapes.

Example
x = 2
y = 5
z = 4

The cats are at positions 2 (Cat A) and 5 (Cat B), and the mouse is at position 4. Cat B, at position 5 will arrive first since it is only 1 unit 
away while the other is 2 units away. Return "Cat B".

- X = cat A's position
- Y = cat B's position
- Z = mouse C's position
'''

x=7
y=9
z=4


def catAndMouse(x, y, z):

    catACounter = 0
    catBCounter = 0

    if z > x and z < y:
        for i in range(x, z):
            catACounter+=1
        for j in range(z, y):
            catBCounter+=1
    
    if z > x and z > y:
        for i in range(x, z):
            catACounter+=1
        for j in range(y, z):
            catBCounter+=1

    if z < x and z < y:
        for i in range(z, x):
            catACounter+=1
        for j in range(z, y):
            catBCounter+=1

    if catACounter > catBCounter:
        print('Cat B')
    elif catBCounter > catACounter:
        print('Cat A')
    else:
        print('Mouse C')
    
def catAndMouse_2(x, y, z):
    a = abs(x-z)
    b = abs(y-z)
        
    return "Cat A" if a<b else "Cat B" if b<a else "Mouse C"


catAndMouse(x, y, z)
