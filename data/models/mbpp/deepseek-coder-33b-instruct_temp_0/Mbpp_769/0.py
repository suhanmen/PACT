Here is the Python function to get the difference between two lists:

```python
def Diff(list1, list2):
    return [i for i in list1 + list2 if i not in list1 or i not in list2]
```

This function works by concatenating the two lists and then using a list comprehension to create a new list that includes only the elements that are not in both lists.

You can test this function with the provided example:

```python
print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]))
```

This should output:

```python
[10, 20, 30, 15]
```
