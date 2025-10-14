Here's the completed code snippet:

```python
def intersection_array(arr1, arr2):
    return list(set(arr1) & set(arr2))

assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9]) == [1, 2, 8, 9]
```

In this code, the `intersection_array` function takes two arrays as input (`arr1` and `arr2`). It converts both arrays into sets using the `set()` function, which removes any duplicate elements. Then, it uses the `&` operator to find the intersection of the two sets, which gives us a new set containing only the common elements. Finally, it converts the set back into a list using the `list()` function and returns the result.

The `assert` statement at the end of the code is used to verify that the function produces the expected output. If the output matches the expected result, the code will continue executing without any errors. Otherwise, it will raise an `AssertionError` indicating that the function is not working correctly.