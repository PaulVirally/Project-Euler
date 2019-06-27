# a^2 + b^2 = c^2
# a + b + c = n
# n = 1000
# 2ab = 2na + 2nb + n^2
# b = [n(n + 2a)] / [2(a-n)]

# b = [1000000 + 2000a] / [2a - 20000]
import math
n = 500
for a in range(1, n):
    for b in range(1, n):
        c = (a**2 + b**2)**0.5
        if (a + b + c) == 1000:
            print(a*b*c) # 31875000.0
            exit()