Here is the completed code snippet:

```python
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    return binary

assert decimal_to_binary(8) == '1000'
```

In this code, the `decimal_to_binary` function takes a decimal number as input and uses the built-in `bin` function to convert it to its binary representation. The `bin` function returns a string with a '0b' prefix, so we use slicing to remove the first two characters and return the binary string. The `assert` statement is used to verify that the function returns the expected result.