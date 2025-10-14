"""
Write a function to calculate the sum (n - 2*i) from i=0 to n // 2, for instance n + (n-2) + (n-4)... (until n-x =< 0).
assert sum_series(6) == 12
"""



def sum_series(n):
    return sum(n - 2*i for i in range(n // 2 + 1))

assert sum_series(6) == 12
