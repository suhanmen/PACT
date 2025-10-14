Here is the Python function to find the maximum difference between any two elements in a given array:

```python
def max_Abs_Diff(arr):
    """
    This function finds the maximum difference between any two elements in a given array.
    """
    # Check if the array is empty
    if len(arr) == 0:
        return 0

    # Initialize the minimum and maximum values
    min_val = arr[0]
    max_val = arr[0]

    # Iterate over the array to find the minimum and maximum values
    for num in arr:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num

    # Return the absolute difference between the maximum and minimum values
    return abs(max_val - min_val)
```

You can test the function with the following code:

```python
print(max_Abs_Diff([2,1,5,3]))  # Output: 4
```

This function works by initializing the minimum and maximum values to the first element of the array. It then iterates over the array, updating the minimum and maximum values as it goes. Finally, it returns the absolute difference between the maximum and minimum values.
