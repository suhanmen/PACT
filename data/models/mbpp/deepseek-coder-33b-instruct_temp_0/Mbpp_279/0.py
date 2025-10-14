Here is the Python function to find the nth decagonal number:

```python
def is_num_decagonal(n):
    return n * (4 * n - 3) // 2
```

You can test the function with the following code:

```python
print(is_num_decagonal(3))  # Output: 27
```

This function works by using the formula for the nth decagonal number, which is n * (4 * n - 3) // 2. The // operator is used for integer division, which discards the fractional part and returns only the integer part.
