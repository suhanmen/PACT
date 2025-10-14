"""
Write a function to sum all amicable numbers from 1 to a specified number.
assert amicable_numbers_sum(999)==504
"""


import math

def sum_of_divisors(n):
    sum = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum += i
            if i != n // i:
                sum += n // i
    return sum

def amicable_numbers_sum(limit):
    amicable_sum = 0
    for a in range(2, limit):
        b = sum_of_divisors(a)
        if b > a and sum_of_divisors(b) == a:
            amicable_sum += a + b
    return amicable_sum

assert amicable_numbers_sum(999) == 504
