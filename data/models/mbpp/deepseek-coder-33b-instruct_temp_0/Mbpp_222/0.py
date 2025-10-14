Here is the Python function that checks if all the elements in a tuple have the same data type or not:

```python
def check_type(t):
    return len(set(type(i) for i in t)) == 1

print(check_type((5, 6, 7, 3, 5, 6)))  # True
```

In this function, we use a set to store the types of the elements in the tuple. If all elements have the same type, the set will only contain one type. Therefore, if the length of the set is 1, we return True, otherwise we return False.
