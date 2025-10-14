Here's the completed code snippet:

```python
def move_zero(lst):
    non_zero = [num for num in lst if num != 0]
    zero = [num for num in lst if num == 0]
    return non_zero + zero
```

This function takes a list as input and creates two separate lists: `non_zero` which contains all the non-zero elements from the input list, and `zero` which contains all the zero elements from the input list. Then, it concatenates `non_zero` and `zero` to get the final list with all the zeroes moved to the end.

The `assert` statement checks if the output of the function matches the expected output.