Here is the completed code snippet:

```python
def median_trapezium(a, b, c):
    """
    Calculates the median length of a trapezium given the lengths of its bases and the length of its height.
    
    Parameters:
    a (float): Length of the first base
    b (float): Length of the second base
    c (float): Length of the height
    
    Returns:
    float: Median length of the trapezium
    """
    return (a + b) / 2

assert median_trapezium(15, 25, 35) == 20
```

In this code, the `median_trapezium` function takes three parameters: `a`, `b`, and `c`. These parameters represent the lengths of the trapezium's bases (`a` and `b`) and its height (`c`).

The function then calculates the median length of the trapezium by adding the lengths of the two bases (`a` and `b`) and dividing the sum by 2. This is done using the formula `(a + b) / 2`.

Finally, the function returns the calculated median length.

The `assert` statement at the end of the code snippet is used to verify that the function produces the expected result. In this case, it checks if `median_trapezium(15, 25, 35)` is equal to `20`. If the assertion fails, an error will be raised.