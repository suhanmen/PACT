Here is the completed code snippet:

```python
def second_smallest(numbers):
    # Remove duplicates and sort the list in ascending order
    sorted_numbers = sorted(set(numbers))
    
    # Check if the list has at least two elements
    if len(sorted_numbers) < 2:
        return None
    
    # Return the second smallest number
    return sorted_numbers[1]

# Test the function
assert second_smallest([1, 2, -8, -2, 0, -2]) == -2
```

The function `second_smallest` takes a list of numbers as input. It first removes duplicates from the list using the `set` function, and then sorts the resulting list in ascending order using the `sorted` function. If the sorted list has less than two elements, it means there is no second smallest number, so the function returns `None`. Otherwise, it returns the second element of the sorted list, which is the second smallest number.