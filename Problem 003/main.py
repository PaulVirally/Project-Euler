def prime_factors(n):
    is_odd = n % 2
    i = 2
    if is_odd:
        i = 3
    factors = []
    while i * i <= n:
        if n % i != 0:
            if is_odd:
                i += 2
            else:
                i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

print(max(prime_factors(600851475143))) # 6857