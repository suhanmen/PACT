Here is the Python function to find the sublist having minimum length:

```python
def Find_Min(lst):
    return min(lst, key=len)
```

You can test the function with the provided example:

```python
print(Find_Min([[1],[1,2],[1,2,3]]))  # Output: [1]
```

This function uses the built-in `min` function in Python, which returns the smallest item in an iterable or the smallest of two or more arguments. The `key` argument specifies a one-argument ordering function like that used for list.sort(). The `len` function is used as the key function to find the sublist with the minimum length.
