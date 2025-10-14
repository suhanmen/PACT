Here is the Python function that solves the problem:

```python
def re_arrange_array(arr, n):
    neg = [x for x in arr[:n] if x < 0]
    pos = [x for x in arr[:n] if x >= 0]
    return neg + pos + arr[n:]
```

This function first separates the negative and positive elements in the first `n` elements of the array. Then it concatenates the negative elements, the positive elements, and the remaining elements of the array.

Let's test the function with the given example:

```python
print(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9))
```

The output should be:

```python
[-1, -3, -7, 2, 4, 5, 6, 8, 9]
```

This output matches the expected output in the problem statement.
