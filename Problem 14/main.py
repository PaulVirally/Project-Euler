def collatz(n):
    if n % 2 == 0:
        return int(n/2)
    return 3*n + 1

largest = -1
largest_chain = -1
for i in range(1, 1000000):
    c = collatz(i)
    chain_size = 1
    while c is not 1:
        c = collatz(c)
        chain_size += 1
    if chain_size > largest_chain:
        largest = i
        largest_chain = chain_size

print(largest) # 837799