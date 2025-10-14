Here's the completed code snippet:

```python
def find_length(binary_string):
    max_diff = 0
    count_0 = 0
    count_1 = 0

    for char in binary_string:
        if char == '0':
            count_0 += 1
        else:
            count_1 += 1

        diff = count_0 - count_1
        if diff > max_diff:
            max_diff = diff
        elif diff < 0:
            count_0 = 0
            count_1 = 0

    return max_diff

assert find_length("11000010001") == 6
```

In this code, we iterate through each character in the binary string. We keep track of the count of 0s and 1s encountered so far. We calculate the difference between the count of 0s and 1s and update the `max_diff` variable if the current difference is greater than the previous maximum difference. If the difference becomes negative, it means that the count of 1s has exceeded the count of 0s, so we reset the counts to 0.

The function returns the maximum difference between the number of 0s and 1s in any sub-string of the given binary string. The provided assertion checks if the function returns the expected result for the given example.