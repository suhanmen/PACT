Here is the completed code snippet:

```python
def test_duplicate(arr):
    # Convert the array to a set to remove duplicates
    unique_elements = set(arr)
    
    # If the length of the set is equal to the length of the array, there are no duplicates
    if len(unique_elements) == len(arr):
        return False
    else:
        return True

assert test_duplicate([1,2,3,4,5]) == False
```

This function takes an array as input and converts it to a set to remove any duplicate elements. It then compares the length of the set to the length of the original array. If they are equal, it means there are no duplicates and the function returns False. Otherwise, it returns True, indicating that there are duplicate elements in the array. The assert statement at the end verifies that the function works correctly for the given example.