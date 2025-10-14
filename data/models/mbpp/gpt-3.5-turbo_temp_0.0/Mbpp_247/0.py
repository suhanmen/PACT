Here is the completed code snippet:

```python
def lps(string):
    n = len(string)
    # Create a table to store the lengths of longest palindromic subsequences
    table = [[0] * n for _ in range(n)]

    # All substrings of length 1 are palindromes of length 1
    for i in range(n):
        table[i][i] = 1

    # Build the table in bottom-up manner
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if string[i] == string[j] and cl == 2:
                table[i][j] = 2
            elif string[i] == string[j]:
                table[i][j] = table[i + 1][j - 1] + 2
            else:
                table[i][j] = max(table[i][j - 1], table[i + 1][j])

    # The length of the longest palindromic subsequence is at table[0][n-1]
    return table[0][n - 1]


assert lps("TENS FOR TENS") == 5
```

The function `lps` uses dynamic programming to find the length of the longest palindromic subsequence in the given string. It creates a table to store the lengths of palindromic subsequences for all substrings of the input string. The table is filled in a bottom-up manner, starting with substrings of length 1 and gradually increasing the length until the entire string is considered.

The function then returns the length of the longest palindromic subsequence, which is stored at `table[0][n-1]`, where `n` is the length of the input string.

The provided test case `assert lps("TENS FOR TENS") == 5` verifies that the function returns the correct result for the given example.