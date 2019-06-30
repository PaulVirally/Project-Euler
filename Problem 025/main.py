a = 1
b = 1
num = 2

while b < 10**999:
    a, b = b, a+b
    num += 1
print(num) # 4782