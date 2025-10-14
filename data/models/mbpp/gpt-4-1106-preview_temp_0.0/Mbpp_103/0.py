"""
Write a function to find the Eulerian number a(n, m).
assert eulerian_num(3, 1) == 4
"""


import math

def eulerian_num(n, m):
    # A recursive function to find the Eulerian number A(n, m)
    if m >= n or n == 0:
        return 0
    if m == 0:
        return 1
    if m == n-1:
        return math.factorial(n-1)
    return (n-m) * eulerian_num(n-1, m-1) + (m+1) * eulerian_num(n-1, m)

# Example usage:
# assert eulerian_num(3, 1) == 4
