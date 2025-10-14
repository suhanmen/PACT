Here is the Python function to compute the n-th power of each number in a list:

```python
def nth_nums(nums, n):
    return [num ** n for num in nums]
```

You can test this function with the following code:

```python
print(nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2))
```

This will output:

```python
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
