"""
Write a function to find the maximum sum possible by using the given equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n).
assert get_max_sum(60) == 106
"""


import functools

def get_max_sum(n):
    @functools.lru_cache(maxsize=None)
    def max_sum(n):
        if n == 0:
            return 0
        return max(max_sum(n//2) + max_sum(n//3) + max_sum(n//4) + max_sum(n//5), n)
    
    return max_sum(n)

assert get_max_sum(60) == 106
