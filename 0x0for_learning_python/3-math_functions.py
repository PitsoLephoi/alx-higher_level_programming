#!/usr/bin/env python3

def add(a, b):
    return a + b

def is_even(n):
    if n % 2 == 0:
        return True
    return False

sum = add(3, 4)
result = is_even(10)

print(sum)
print(result)