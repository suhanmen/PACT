"""
Write a function to find the length of the longest palindromic subsequence in the given string.
assert lps("TENS FOR TENS") == 5
"""


import functools

def lps(s):
    @functools.lru_cache(maxsize=None)
    def dp(l, r):
        if l > r: return 0
        if l == r: return 1
        if s[l] == s[r]:
            return 2 + dp(l + 1, r - 1)
        return max(dp(l + 1, r), dp(l, r - 1))
    return dp(0, len(s) - 1)

assert lps("TENS FOR TENS") == 5
