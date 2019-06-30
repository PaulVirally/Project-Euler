'''
0 1 2 -, 2 permutations = 2! = (3-1) permutations
0 2 1 -'
1 0 2 -, 2 permutations
1 2 0 -'
2 0 1 -, 2 permutations
2 1 0 -'

0 1 2 3 -, 6 perms = 3! = (4-1)! permutations
0 1 3 2  |
0 2 1 3  |
0 2 3 1  |
0 3 1 2  |
0 3 2 1 -'
1 0 2 3 -, 6 perms
1 0 3 2  |
1 2 0 3  |
1 2 3 0  |
1 3 0 2  |
1 3 2 0 -'

With n digits, we go by chunks of (n-1)! permutations
So with 10 digits we go by 9! = 362 880 permutations
Therefore the first digit will be 2 since after 2 chunks we have done 725 760 permutations
and after 3 chunks we have done 1 088 640 (too many) permutations
Number: 2 _ _ _ _ _ _ _ _ _

Now we have the digits 0, 1, 3, 4, 5, 6, 7, 8, 9
With 9 digits, we go by 8! = 40 230 permutations
725760 + k*40230 < 1 000 000
k = 6
725760 + 6*40230 = 967 140
Therefore the second digit will be on 6+1 = 7 chunk
0 1 3 4 5 6 7 8 9
            ^
Number: 2 7 _ _ _ _ _ _ _ _

Now we have the digits 0, 1, 3, 4, 5, 6, 8, 9
With 8 digits we go by 7! = 5 040 permutations
967140 + k*5040 < 1 000 000
k = 6
967140 + 6*5040 = 997 380
Therefore the third digit will be on the 6+1 = 7 chunk
0 1 3 4 5 6 8 9
            ^
Number: 2 7 8 _ _ _ _ _ _ _

Now we have the digits 0, 1, 3, 4, 5, 6, 9
With 7 digits we go by 6! = 720 permutations
997380 + k*720 < 1 000 000
k = 3
997380 + 3*720 = 999 540
Therefore the fourth digit will be on the 3+1 = 4 chunk
0 1 3 4 5 6 9
      ^
Number: 2 7 8 4 _ _ _ _ _ _

Now we have the digits 0, 1, 3, 5, 6, 9
With 6 digits we go by 5! = 120 permutations
999540 + k*120 < 1 000 000
k = 3
999540 + 3*120 = 999 900
Therefore the fifth digit will be on the 3+1 = 4 chunk
0 1 3 5 6 9
      ^
Number: 2 7 8 4 5 _ _ _ _ _

Now we have the digits 0, 1, 3, 6, 9
With 5 digits we go by 4! = 24 permutations
999900 + k*24 < 1 000 000
k = 4
999900 + 4*24 = 999 996
Therefore the sixth digit will be on the 4+1 = 5 chunk
0 1 3 6 9
        ^
Number: 2 7 8 4 5 9 _ _ _ _

Now we have the digits 0, 1, 3, 6
With 4 digits we go by 3! = 6 permutations
999996 + k*6 < 1 000 000
k = 0
999996 + 0*24 = 999 996
Therefore the seventh digit will be on the 0+1 = 1 chunk
0 1 5 8 9
^
Number: 2 7 8 4 5 9 0 _ _ _

Apparently I must have messed up somewhere in my arithmetic since
the code version of what I am doing above gives a different answer
and the correct answer.
'''

def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

result = ''
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
perms_so_far = 0
for i in range(9): # Runs in O(n) with n being number of digits
    adder = factorial(len(digits) - 1)
    count = 0
    while perms_so_far < 1000000:
        perms_so_far += adder
        count += 1
    perms_so_far -= adder
    count -= 1

    digit = digits[count]
    result += str(digit)
    digits.remove(digit)

result += str(digits[0])
print(result) # 2783915460