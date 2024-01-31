#!/usr/bin/python3
"""
Script that computes a minimum operations
needed in a CopyAll - Paste task
"""

def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            n //= divisor
            operations += divisor
        else:
            divisor += 1

    return operations

# Example usage:
n = 9
print("Min number of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min number of operations to reach {} char: {}".format(n, minOperations(n)))
