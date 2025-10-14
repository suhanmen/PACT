Here is the Python function implemented in a markdown style code block:

```python
def common_element(list1, list2):
    for i in list1:
        if i in list2:
            return True
    return False
```

You can test the function with the provided test case:

```python
print(common_element([1,2,3,4,5], [5,6,7,8,9]))  # Output: True
```
