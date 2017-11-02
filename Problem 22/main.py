values = {}
for i in range(65, 90+1):
    values[chr(i)] = i-65 + 1

def alphabetical_value(s):
    val = 0
    for letter in s:
        val += values[letter]
    return val

with open('./names.txt') as in_file:
    names = in_file.read().split(',')

names.sort()
total = 0
for i in range(len(names)):
    total += alphabetical_value(names[i]) * (i+1)

print(total) # 871198282