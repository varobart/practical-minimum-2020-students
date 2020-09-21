#!/usr/local/bin/python3
import random

test_count = 63

for _ in range(test_count):
    a = str(random.randint(10, 99))
    b = str(random.randint(10, 99))
    op = '+' if random.randint(0, 1) == 0 else '-'
    print(a, op, b)

