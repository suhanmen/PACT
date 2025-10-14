Here is the Python function to solve the problem:

```python
def extract_rear(tup):
    return [s[-1] for s in tup]
```

You can test the function with the given example:

```python
print(extract_rear(('Mers', 'for', 'Vers')))  # Output: ['s', 'r', 's']
```

This function uses a list comprehension to iterate over each string in the tuple, and for each string, it takes the last character (`s[-1]`) and adds it to the new list.
