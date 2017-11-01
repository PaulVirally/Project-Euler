def fac(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod

def sum_digits(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

print(sum_digits(fac(100))) # 648