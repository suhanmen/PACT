Here is the completed code snippet:

```python
def sort_counter(dictionary):
    sorted_dict = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return sorted_dict

assert sort_counter({'Math':81, 'Physics':83, 'Chemistry':87}) == [('Chemistry', 87), ('Physics', 83), ('Math', 81)]
```

The `sort_counter` function takes a dictionary as input and uses the `sorted` function to sort the dictionary items based on their values. The `key` parameter is set to `lambda x: x[1]` to specify that the sorting should be based on the second element of each item (the value). The `reverse` parameter is set to `True` to sort the items in descending order. The sorted dictionary is then returned. The `assert` statement is used to verify that the function produces the expected output.