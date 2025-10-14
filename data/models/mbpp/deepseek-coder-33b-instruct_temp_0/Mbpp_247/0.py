Here is the Python function to find the length of the longest palindromic subsequence in the given string.

```python
def lps(s):
    n = len(s)
    # Create a table to store lengths of longest palindromic subsequences
    dp = [[0]*n for _ in range(n)]

    # Strings of length 1 are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Fill dp[][] in bottom up manner
    for cl in range(2, n+1):
        for i in range(n-cl+1):
            j = i+cl-1
            if s[i] == s[j] and cl == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])

    return dp[0][n-1]

# Test the function
print(lps("TENS FOR TENS"))  # Output: 5
```

This function uses dynamic programming to solve the problem. It first initializes a 2D array `dp` where `dp[i][j]` stores the length of the longest palindromic subsequence in the substring `s[i..j]`. It then fills up this table in a bottom-up manner. The final answer is stored in `dp[0][n-1]`.
