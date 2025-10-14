Here is the Python function that performs the division operation element-wise across the given tuples:

```python
def division_elements(tuple1, tuple2):
    return tuple(a / b for a, b in zip(tuple1, tuple2))
```

You can test the function with the provided example:

```python
print(division_elements((10, 4, 6, 9), (5, 2, 3, 3)))  # Output: (2.0, 2.0, 2.0, 3.0)
```

Please note that the function uses the `zip` function to iterate over the two tuples simultaneously. The `/` operator is used for division. The `tuple` function is used to convert the result back into a tuple.
