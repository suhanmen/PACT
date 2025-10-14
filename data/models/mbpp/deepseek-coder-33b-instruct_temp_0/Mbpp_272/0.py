Here is the Python function in a markdown style code block:

```python
def rear_extract(tuples_list):
    return [t[-1] for t in tuples_list]
```

This function uses a list comprehension to iterate over each tuple in the input list. For each tuple, it takes the last element (`t[-1]`) and adds it to the new list.

You can test this function with the provided example:

```python
print(rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]))
```

This should output:

```python
[21, 20, 19]
```
