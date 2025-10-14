Here is the Python function to find the median length of a trapezium:

```python
def median_trapezium(a, b, c):
    """
    This function calculates the median length of a trapezium.
    It takes three arguments: a, b, and c, which are the lengths of the parallel sides of the trapezium.
    """
    return (a + b + c - max(a, b, c) - min(a, b, c)) / 2

# Test the function
assert median_trapezium(15,25,35)==20
```

This function works by first finding the sum of the lengths of the two parallel sides (a and b) and the sum of the lengths of the two non-parallel sides (b and c). It then subtracts the maximum and minimum of these two sums to get the length of the median. Finally, it divides this length by 2 to get the median length.
