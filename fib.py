#!/usr/bin/env python

def fib(n):
    a, b = 1, 1
    while n > 1:
        a, b = b, a+b
        n -= 1
    return a


result = [fib(x) for x in range(1,10)]
for v in result:
    print(v)

