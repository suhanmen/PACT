Here is the Python function to rotate left bits by d bits a given number:

```python
def left_rotate(n, d):
    return (n << d)|(n >> (32 - d))

# Test the function
assert left_rotate(16,2) == 64
```

This function uses bitwise shift operators to rotate the bits of the number. The `<<` operator shifts the bits of the number to the left by d places, and the `>>` operator shifts the bits to the right by (32 - d) places. The `|` operator is then used to combine the two results, effectively rotating the bits of the number to the left by d places.
