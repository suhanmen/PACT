"""
Write a function to find the next smallest palindrome of a specified integer, returned as an integer.
assert next_smallest_palindrome(99)==101
"""


import math

def next_smallest_palindrome(num):
    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    if num < 0:
        return None

    num += 1
    while not is_palindrome(num):
        num += 1
    return num

assert next_smallest_palindrome(99) == 101
