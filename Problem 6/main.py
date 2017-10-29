# 1  + 2  + 3  + ... + n  = 1/2 * n(n+1)
# 1² + 2² + 3² + ... + n² = 1/6 * n(n+1)(2n+1)

n = 100

s1 = (1/2 * n * (n+1)) ** 2
s2 = 1/6 * n * (n+1) * (2*n+1)
print(s1, s2, s1-s2) # 25164150.0