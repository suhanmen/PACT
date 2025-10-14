Here is the Python function to convert tuple string to integer tuple:

```python
def tuple_str_int(tuple_str):
    return tuple(map(int, tuple_str[1:-1].split(', ')))
```

You can use this function as follows:

```python
print(tuple_str_int("(7, 8, 9)"))  # Output: (7, 8, 9)
```

This function works by first removing the parentheses from the string using `tuple_str[1:-1]`, then splitting the string into a list of strings using `split(', ')`, and finally converting each string to an integer using `map(int, ...)`. The resulting list of integers is then converted back to a tuple using `tuple(...)`.
