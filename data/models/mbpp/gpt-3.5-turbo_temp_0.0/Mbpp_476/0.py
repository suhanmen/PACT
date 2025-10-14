Here is the completed code snippet:

```python
def big_sum(arr):
    smallest = min(arr)
    largest = max(arr)
    return smallest + largest

assert big_sum([1,2,3]) == 4
```

In this code, the `big_sum` function takes an array as input. It uses the `min` function to find the smallest value in the array and the `max` function to find the largest value. Then, it returns the sum of the smallest and largest values. The `assert` statement is used to verify that the function returns the expected result.