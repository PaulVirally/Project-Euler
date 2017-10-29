def is_prime(n):
    if n < 2:
        return False

    elif n < 4:
        return True

    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i**2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

i = 1
n = 0
while n < 10001:
    i += 1
    if is_prime(i):
        n += 1
print(i) # 104743