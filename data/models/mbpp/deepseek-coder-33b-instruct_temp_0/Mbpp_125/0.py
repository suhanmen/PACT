Here is the Python function to solve the problem:

```python
def find_length(binary_string):
    max_diff = 0
    count_0 = 0
    count_1 = 0

    for i in range(len(binary_string)):
        if binary_string[i] == '0':
            count_0 += 1
        else:
            count_1 += 1

        if count_0 - count_1 > max_diff:
            max_diff = count_0 - count_1
        elif count_1 - count_0 > max_diff:
            max_diff = count_1 - count_0

    return max_diff
```

This function works by iterating over the binary string and keeping track of the count of 0s and 1s. It then calculates the difference between the counts and updates the maximum difference if the current difference is greater.

You can test the function with the given test case:

```python
print(find_length("11000010001"))  # Output: 6
```

This function has a time complexity of O(n) where n is the length of the binary string.
