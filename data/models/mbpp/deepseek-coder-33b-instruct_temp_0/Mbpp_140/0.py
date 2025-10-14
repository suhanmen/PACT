Here is the Python function to flatten the list of lists into a single set of numbers:

```python
def extract_singly(list_of_lists):
    return set([num for sublist in list_of_lists for num in sublist])
```

You can test the function with the following code:

```python
print(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)]))
```

This will output:

```python
{1, 3, 4, 5, 7}
```

This output is a set of unique numbers from the input list of lists.
