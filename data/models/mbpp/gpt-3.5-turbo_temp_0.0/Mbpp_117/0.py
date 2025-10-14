Here is the completed code snippet:

```python
def list_to_float(lst):
    result = []
    for inner_lst in lst:
        converted_inner_lst = []
        for element in inner_lst:
            try:
                converted_inner_lst.append(float(element))
            except ValueError:
                converted_inner_lst.append(element)
        result.append(tuple(converted_inner_lst))
    return result

assert list_to_float([("3", "4"), ("1", "26.45"), ("7.32", "8"), ("4", "8")]) == [(3.0, 4.0), (1.0, 26.45), (7.32, 8.0), (4.0, 8.0)]
```

The `list_to_float` function takes a list of tuples as input. It iterates over each tuple in the list and converts each element to a float if it is convertible. If an element cannot be converted to a float, it is left unchanged. The function returns a new list of tuples with the converted elements.