Here is the Python function to solve the problem:

```python
def sort_sublists(lst):
    return [sorted(sublist) for sublist in lst]
```

This function uses a list comprehension to iterate over each sublist in the given list. The `sorted` function is then used to sort each sublist. The result is a new list of sorted sublists.

You can test the function with the provided example:

```python
print(sort_sublists([["green", "orange"], ["black", "white"], ["white", "black", "orange"]]))
```

This should output:

```python
[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
```
