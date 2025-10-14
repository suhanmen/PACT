Here is the completed code snippet:

```python
def max_sub_array_sum(arr, n):
    max_sum = float('-inf')
    current_sum = 0

    for i in range(n):
        current_sum += arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0

    return max_sum

assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
```

The function `max_sub_array_sum` takes in a list `arr` and its length `n`. It initializes `max_sum` and `current_sum` to negative infinity and 0, respectively. It then iterates through the list, adding each element to `current_sum`. If `current_sum` becomes greater than `max_sum`, `max_sum` is updated. If `current_sum` becomes negative, it is reset to 0. Finally, the function returns `max_sum`.

The `assert` statement checks if the function returns the expected result for the given example.