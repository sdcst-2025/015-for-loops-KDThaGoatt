#! python3
"""
##### Task 3
Print all the numbers from 1 to 1000 that are divisible by 5.
"""

x = 1

for x in range(1, 1001):
    if x % 5 == 0:
        print(x)
    x = x + 1
