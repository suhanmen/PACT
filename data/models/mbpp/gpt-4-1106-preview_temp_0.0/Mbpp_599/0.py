"""
Write a function to find sum and average of first n natural numbers.
assert sum_average(10)==(55, 5.5)
"""



def sum_average(n):
    sum_n = n * (n + 1) // 2
    average_n = sum_n / n
    return sum_n, average_n

assert sum_average(10) == (55, 5.5)
