Here is the completed code snippet:

```python
def rear_extract(lst):
    return [t[-1] for t in lst]

assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]
```

The function `rear_extract` takes in a list of tuples `lst`. It uses a list comprehension to iterate over each tuple in the list and extract the last element of each tuple using `t[-1]`. The extracted elements are then returned as a new list. The `assert` statement checks if the function returns the expected output.