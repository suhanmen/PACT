Here is the Python function that calculates the sum of all digits of the base to the specified power:

```python
def power_base_sum(base, power):
    result = base ** power
    return sum(int(digit) for digit in str(result))

# Test the function
assert power_base_sum(2,100)==115
```

This function first calculates the result of the base to the power using the `**` operator. Then it converts the result to a string, iterates over each digit in the string, converts it back to an integer, and adds it to the sum.
