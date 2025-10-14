Here is the Python function to solve the problem:

```python
def test_duplicate(arr):
    """
    Function to find whether a given array of integers contains any duplicate element.
    """
    return len(arr) != len(set(arr))

# Test the function
print(test_duplicate([1,2,3,4,5])) # Expected output: False
```

In this function, we are using a property of sets in Python. A set is an unordered collection of unique elements. By converting the list to a set, we automatically remove any duplicate elements. If the length of the set is not equal to the length of the original list, it means there were duplicate elements in the list.
