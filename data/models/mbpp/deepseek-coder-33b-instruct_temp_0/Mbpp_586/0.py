Here is the Python function to solve the problem:

```python
def split_Arr(arr, n):
    return arr[n:] + arr[:n]
```

You can test the function with the provided test case:

```python
print(split_Arr([12,10,5,6,52,36],2))
```

This should return: `[5,6,52,36,12,10]`
