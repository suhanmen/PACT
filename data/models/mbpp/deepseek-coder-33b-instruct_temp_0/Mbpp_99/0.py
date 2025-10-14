Here is the Python function to convert the given decimal number to its binary equivalent:

```python
def decimal_to_binary(n):
    return bin(n).replace("0b", "")
```

You can test the function with the following code:

```python
print(decimal_to_binary(8))  # Output: '1000'
```

This function uses the built-in `bin()` function in Python, which converts an integer number to a binary string. The `replace("0b", "")` part is used to remove the '0b' prefix that Python adds to binary numbers.
