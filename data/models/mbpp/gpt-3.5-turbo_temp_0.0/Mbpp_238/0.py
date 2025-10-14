Here is the completed code snippet:

```python
def number_of_substrings(string):
    n = len(string)
    return n * (n + 1) // 2

assert number_of_substrings("abc") == 6
```

The function `number_of_substrings` takes a string as input and returns the number of non-empty substrings of that string. It uses the formula `n * (n + 1) // 2`, where `n` is the length of the string, to calculate the number of substrings. The `//` operator is used for integer division to ensure that the result is an integer. The code also includes an assertion to verify that the function returns the expected result for the given example.