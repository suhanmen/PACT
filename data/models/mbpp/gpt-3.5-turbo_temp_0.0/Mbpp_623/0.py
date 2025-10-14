Here is the completed code snippet:

```python
def nth_nums(nums, n):
    return [num ** n for num in nums]

assert nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

The `nth_nums` function takes in a list of numbers `nums` and an integer `n`. It uses a list comprehension to compute the `n`-th power of each number in the list and returns the resulting list. The `assert` statement checks if the function produces the expected output for the given example.