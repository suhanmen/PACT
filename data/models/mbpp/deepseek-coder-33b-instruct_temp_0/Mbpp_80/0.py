Here is the Python function to find the nth tetrahedral number:

```python
def tetrahedral_number(n):
    return n * (n + 1) * (n + 2) // 6
```

You can test the function with the following code:

```python
assert tetrahedral_number(5) == 35
```

This function works by using the formula for the nth tetrahedral number, which is n * (n + 1) * (n + 2) // 6. The // operator is used for integer division, which discards the remainder and only keeps the quotient.
