Here is the Python function that returns the number of integer elements in a given list:

```python
def count_integer(lst):
    count = 0
    for i in lst:
        if type(i) == int:
            count += 1
    return count
```

You can test the function with the following code:

```python
print(count_integer([1,2,'abc',1.2]))  # Output: 2
```

This function works by iterating over each element in the list and checking if the type of the element is `int`. If it is, it increments the count. Finally, it returns the count.
