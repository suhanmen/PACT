"""
Write a function to find the nth newman–shanks–williams prime number.
assert newman_prime(3) == 7
"""


import sympy

def newman_prime(n):
    def nswp(k):
        if k == 0:
            return 1
        elif k == 1:
            return 1
        else:
            return 2 * nswp(k - 1) + nswp(k - 2)

    count = 0
    k = 0
    while True:
        candidate = nswp(k)
        if sympy.isprime(candidate):
            count += 1
            if count == n:
                return candidate
        k += 1

assert newman_prime(3) == 7
