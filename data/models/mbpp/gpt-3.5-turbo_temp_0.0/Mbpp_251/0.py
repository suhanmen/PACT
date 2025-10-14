Here is the completed code snippet:

```python
def insert_element(lst, element):
    result = []
    for item in lst:
        result.append(element)
        result.append(item)
    return result

assert insert_element(['Red', 'Green', 'Black'], 'c') == ['c', 'Red', 'c', 'Green', 'c', 'Black']
```

The function `insert_element` takes in a list `lst` and an element `element`. It creates an empty list `result` to store the resulting list. Then, it iterates over each item in `lst` and appends `element` and the current item to `result`. Finally, it returns `result`.

The assertion statement checks if the function returns the expected result when called with the given example inputs.