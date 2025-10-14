Here is the completed code snippet:

```python
def is_Monotonic(arr):
    increasing = decreasing = True

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        if arr[i] < arr[i - 1]:
            increasing = False

    return increasing or decreasing

assert is_Monotonic([6, 5, 4, 4]) == True
```

The function `is_Monotonic` takes an array `arr` as input and checks whether the array is monotonic or not. It uses two boolean variables `increasing` and `decreasing` to keep track of whether the array is increasing or decreasing.

The function iterates through the array starting from the second element. If the current element is greater than the previous element, it sets `decreasing` to False. If the current element is less than the previous element, it sets `increasing` to False.

Finally, the function returns `True` if either `increasing` or `decreasing` is `True`, indicating that the array is monotonic. Otherwise, it returns `False`.

The `assert` statement at the end of the code snippet verifies that the function returns the expected result for the given example input.