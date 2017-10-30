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

total = 0
for i in range(2000000):
    if is_prime(i):
        total += i
print(total) # 142913828922