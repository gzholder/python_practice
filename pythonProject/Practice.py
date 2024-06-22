import math
import os
import random
import re
import sys

n = int(input().strip())
if (n % 2) == 1:
    print("Weird")
# task 2
elif (n % 2) == 0 and n >= 2 and n <= 5:
    print("Not weird")
#task 3
elif n % 2 == 0 and n >= 6 and n <= 20:
    print("Weird")
#task 4
elif n % 2 == 0 and n > 20:
    print("Not weird")

def is_leap(year):
    leap = False
    if (year % 4) == 0:
        leap = True
        if (year % 100) == 0:
            leap = False
        if (year % 400) == 0:
            leap = True
    else:
        leap = False

    return leap


year = int(input())
print(is_leap(year))

n = 3
m = n + 1
for i in range(1, m):
    print(i, end = " ")