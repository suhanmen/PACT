Here is the Python function implemented in a markdown style code block:

```python
def diff_even_odd(numbers):
    """
    Write a function to find the difference of the first even and first odd number of a given list.
    """
    even = None
    odd = None
    for num in numbers:
        if num % 2 == 0 and even is None:
            even = num
        elif num % 2 != 0 and odd is None:
            odd = num
        if even is not None and odd is not None:
            break
    if even is None or odd is None:
        return None
    return even - odd

# Test the function
print(diff_even_odd([1,3,5,7,4,1,6,8]))  # Output: 3
```

This function works by iterating over the list of numbers. It keeps track of the first even and first odd number it encounters. Once it has found both a first even and a first odd number, it breaks out of the loop. If it doesn't find both a first even and a first odd number, it returns None. Otherwise, it returns the difference between the first even and first odd number.
