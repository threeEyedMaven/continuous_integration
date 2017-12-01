#! /usr/bin/env python3
def fibonacci(n):
    if not isinstance(n, int):
        raise TypeError
    if n == 1: return 0
    a = 0
    b = 1
    for i in range(n - 2):
        a, b = b, a + b
    return b

def integerSum(n):
    if not isinstance(n, int):
        raise TypeError
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    return sum

def sum(value1, value2):
    if not isinstance(value1, int) or not isinstance(value2, int):
        raise TypeError
    return value1 + value2
