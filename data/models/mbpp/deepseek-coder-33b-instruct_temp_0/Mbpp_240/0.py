Here is the Python function that solves the problem:

```python
def replace_list(list1, list2):
    list1[-1] = list2
    return list1
```

This function takes in two lists as arguments. It replaces the last element of the first list with the elements of the second list. The `-1` index in Python refers to the last element of the list. The function then returns the modified list.

You can test the function with the provided example:

```python
print(replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8]))
```

This should output:

```python
[1, 3, 5, 7, 9, [2, 4, 6, 8]]
```

This is because the last element of the first list is replaced with the entire second list. If you want to flatten the list, you can modify the function like this:

```python
def replace_list(list1, list2):
    list1[-1:] = list2
    return list1
```

Now, the function should output:

```python
[1, 3, 5, 7, 9, 2, 4, 6, 8]
```
