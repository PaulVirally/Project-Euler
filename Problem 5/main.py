# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# 1 2 3   5   7        11    13          17    19
#       4=2*2 <-- add *2
#           6=3*2 <-- add nothing
#               8=4*2 <-- add *2
#                 9=3*3 <-- add *3
#                   10=5*2 <-- add nothing
#                         12=6*2 <-- add nothing
#                               14=7*2 <-- add nothing
#                                     16=8*2 <-- add *2
#                                           18=9*2 <-- add nothing
#                                                 20=10*2 <-- add nothing
print(1 * 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 2 * 2 * 3 * 2)