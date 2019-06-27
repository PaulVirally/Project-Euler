def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

largest = -1
for a in range(999, 99, -1):
    for b in range(999, 99, -1):
        prod = a * b
        if is_palindrome(prod) and prod > largest:
            largest = prod
print(largest)