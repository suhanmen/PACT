Here is the completed code snippet:

```python
def positive_count(arr):
    positive_nums = [num for num in arr if num > 0]
    ratio = len(positive_nums) / len(arr)
    return round(ratio, 2)

assert positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]) == 0.54
```

In this code, we define a function `positive_count` that takes an array `arr` as input. We use a list comprehension to create a new list `positive_nums` that contains only the positive numbers from `arr`. Then, we calculate the ratio of the length of `positive_nums` to the length of `arr`. Finally, we round the ratio to two decimal places and return it.

The `assert` statement is used to check if the output of the function matches the expected result. In this case, we are asserting that `positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])` should be equal to `0.54`.