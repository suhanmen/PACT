Here is the Python function implemented in a markdown style code block:

```python
def all_Characters_Same(input_string):
    """
    This function checks whether all the characters in a string are the same.
    """
    return len(set(input_string)) == 1

# Test the function
print(all_Characters_Same("python"))  # Output: False
```

In this function, we convert the input string into a set. A set in Python is an unordered collection of unique elements. By converting the string into a set, we automatically remove any duplicate characters. If the length of the set is 1, it means all characters in the string are the same. If the length is not 1, it means there are different characters in the string.
