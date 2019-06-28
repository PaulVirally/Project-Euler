'''
For a 2x2
=========

1100
1010
1001
0110 -- Flipped bits version of above
0101
0110
0011

You have 4 bits
You have 2 1s and 2 0s

The number of numbers with such conditions are
4 choose 2
4 bits, choose 2 1s

For a 3x3
=========

111000
110100
110010
110001
101100
101010
101001
100110
100101
100011
011100 -- Flipped bits version of above
011010
011001
010110
010101
010011
001110
001101
001011
000111

You have 6 bits
You have 3 1s and 3 0s

The number of numbers with such conditions are
12 choose 6
12 bits, choose 6 1s

In general:
2n choose n
'''

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def choose(n, k):
    return factorial(n)/(factorial(n-k) * factorial(k))

grid_size = 20
print(choose(2*grid_size, grid_size)) # 137846528820