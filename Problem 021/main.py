import math
def sum_divisors(n):
    divisors = []
    for i in range(1, math.floor(math.sqrt(n) + 1)):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n//i)

    return sum(divisors) - n

amicable_sum = 0
to_skip = []
for i in range(10000):
    if i in to_skip:
        continue

    a = sum_divisors(i)
    b = sum_divisors(a)
    to_skip.append(a)

    if i == b:
        amicable_sum += a + b

print(amicable_sum) # 48944