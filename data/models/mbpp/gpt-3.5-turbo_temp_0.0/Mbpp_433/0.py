Here is the completed code snippet:

```python
def check_greater(arr, num):
    for element in arr:
        if num <= element:
            return False
    return True

assert check_greater([1, 2, 3, 4, 5], 4) == False
```

The `check_greater` function takes in an array `arr` and a number `num`. It iterates through each element in the array and checks if `num` is less than or equal to the current element. If it finds an element that is greater than or equal to `num`, it returns `False`. If it reaches the end of the array without finding any such element, it returns `True`.

The `assert` statement at the end of the code snippet verifies that the function behaves as expected for the given example.