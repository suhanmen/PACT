Here is the Python function to remove consecutive duplicates from a given list:

```python
def remove_consecutive_duplicates(lst):
    new_lst = [lst[i] for i in range(len(lst)) if i == 0 or lst[i] != lst[i-1]]
    return new_lst

# Test the function
print(remove_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ]))
```

This function works by creating a new list that includes the first element of the original list and then includes any element that is not equal to the previous element in the original list. The `range(len(lst))` generates indices for the list, and `lst[i] != lst[i-1]` checks if the current element is not equal to the previous element. The `or i == 0` part is to include the first element of the list.

When you run this code, it will print:

```python
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
```

which is the list with consecutive duplicates removed.
