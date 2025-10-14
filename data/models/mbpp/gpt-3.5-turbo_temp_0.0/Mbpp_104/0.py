Here is the completed code snippet:

```python
def sort_sublists(lst):
    for sublist in lst:
        sublist.sort()
    return lst

assert sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"])) == [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
```

The `sort_sublists` function takes a list of lists as input. It iterates over each sublist and sorts it using the `sort` method. Finally, it returns the sorted list of lists. The `assert` statement checks if the function produces the expected output.