Here is the Python function to count the occurrence of all elements of a list in a tuple:

```python
def count_Occurrence(tup, lst):
    count = 0
    for i in tup:
        if i in lst:
            count += 1
    return count
```

You can test the function with the provided example:

```python
print(count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b']))  # Output: 3
```

This function works by iterating over each element in the tuple and checking if it is in the list. If it is, it increments a counter. Finally, it returns the counter, which represents the number of occurrences of elements from the list in the tuple.
