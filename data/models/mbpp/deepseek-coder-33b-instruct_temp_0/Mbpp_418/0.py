Here is the Python function to find the element of a list having maximum length:

```python
def Find_Max(lst):
    return max(lst, key=len)
```

You can test the function with the provided example:

```python
print(Find_Max([['A'],['A','B'],['A','B','C']]))  # Output: ['A','B','C']
```

This function works by using the built-in `max` function in Python, which returns the maximum item in an iterable or the maximum of two or more arguments. The `key` argument specifies a function of one argument that is used to extract a comparison key from each element in the list. In this case, we use the built-in `len` function to get the length of each sublist.
