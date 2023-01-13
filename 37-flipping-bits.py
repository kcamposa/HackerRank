
n = 9

def flippingBits(n):
    seq = format(n, '032b')
    print(int(''.join(['0' if bit == '1' else '1' for bit in seq]), 2))
    return int(''.join(['0' if bit == '1' else '1' for bit in seq]), 2)
    

if __name__ == '__main__':
    flippingBits(n)