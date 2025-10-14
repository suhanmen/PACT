Here's the completed code snippet:

```python
"""
Write a python function to find the index of smallest triangular number with n digits. https://www.geeksforgeeks.org/index-of-smallest-triangular-number-with-n-digits/
assert find_Index(2) == 4
"""

def find_Index(n):
    index = 1
    triangular_number = 1
    while len(str(triangular_number)) < n:
        index += 1
        triangular_number += index
    return index

assert find_Index(2) == 4
```

The `find_Index` function takes an integer `n` as input and returns the index of the smallest triangular number with `n` digits. It uses a while loop to generate triangular numbers and checks the length of each number until it finds a triangular number with `n` digits. The function then returns the index of that triangular number.

The assert statement at the end verifies that the function returns the expected result for the given test case.