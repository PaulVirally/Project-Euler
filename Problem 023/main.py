import math
def sum_divisors(n):
    divisors = []
    for i in range(1, math.floor(math.sqrt(n) + 1)):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n//i)

    return sum(divisors) - n

abundant_nums = []
for i in range(2813):
    if sum_divisors(i) > i:
        abundant_nums.append(i)
        
total = 0
for i in range(2813):
    try:
        last_idx = [x for x in abundant_nums if x <= i][-1]
    except IndexError:
        continue
    print(i)

    sub_list = abundant_nums[:last_idx+1]

    found = False
    for j in range(1, i//2 + 1):
        k = i - j
        if j in sub_list and k in sub_list:
            found = True
    if not found:
        total += i
print(total)