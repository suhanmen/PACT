Here is the Python function to find the ratio of positive numbers in an array of integers:

```python
def positive_count(arr):
    positive_numbers = [num for num in arr if num > 0]
    return len(positive_numbers) / len(arr)

# Test the function
print(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]))
```

This function works by first creating a list of only the positive numbers in the input array. It then calculates the ratio of the length of this list to the length of the original array. The `len()` function is used to get the number of elements in a list.

Please note that the function `positive_count` returns a float number, which represents the ratio of positive numbers in the array. The `assert` statement in the problem statement is not valid Python code, it's used to check if the function works as expected.
