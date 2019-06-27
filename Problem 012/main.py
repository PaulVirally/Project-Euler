# Triangle number n = 1/2 n(n+1)

import math
def factors(n):
    factors = []
    for i in range(1, math.floor(math.sqrt(n) + 1)):
        if n % i == 0:
            factors.append(i)
            factors.append(int(n/i))
    return factors

i = 1
while True:
    triangle = i/2 * (i+1)
    if len(factors(triangle)) > 500:
        print(triangle) # 76576500.0
        break
    i += 1