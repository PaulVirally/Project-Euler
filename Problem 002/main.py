a = 0
b = 1
c = 0
total = 0
while c < 4000000:
    c = a + b
    if c % 2 == 0:
        total += c
    a = b
    b = c
print(total) # 4613732