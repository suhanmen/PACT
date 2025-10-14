Here is the completed code snippet:

```python
def check_element(lst, element):
    return all(item == element for item in lst)

assert check_element(["green", "orange", "black", "white"], 'blue') == False
```

The `check_element` function takes in a list `lst` and an element `element`. It uses a list comprehension to iterate over each item in the list and checks if it is equal to the given element. The `all` function is used to check if all items in the list satisfy the condition. The function returns `True` if all items are equal to the element, and `False` otherwise.

The `assert` statement is used to verify that the function behaves as expected. In this case, it checks if the function returns `False` when given the list `["green", "orange", "black", "white"]` and the element `'blue'`.