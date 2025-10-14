Here is the completed code snippet:

```python
def tuple_str_int(tuple_str):
    # Remove the parentheses from the string
    tuple_str = tuple_str.strip("()")

    # Split the string into individual elements
    elements = tuple_str.split(", ")

    # Convert each element to an integer
    int_tuple = tuple(int(element) for element in elements)

    return int_tuple

# Test the function
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
```