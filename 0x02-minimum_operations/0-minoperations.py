#!/usr/bin/python3
"""
Script that computes a minimum operation
check all
"""


def minOperations(n):
    if n <= 1:
        return n

    operations = 0
    clipboard = 1  # Initialize clipboard with one 'H'
    total_H = 1    # Initially, there's one 'H' in the file

    while total_H < n:
        if n % total_H == 0:
            # If the number of 'H' needed is a multiple of the current total_H,
            # perform Copy All operation to duplicate the current sequence
            operations += 1
            clipboard = total_H
            total_H *= 2
        else:
            # Paste from clipboard
            operations += 1
            total_H += clipboard

    return operations

# Example usage:
n = 9
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
