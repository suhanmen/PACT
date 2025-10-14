Here is the completed code snippet:

```python
def unique_sublists(lst):
    count_dict = {}
    for sublist in lst:
        sublist_tuple = tuple(sublist)
        if sublist_tuple in count_dict:
            count_dict[sublist_tuple] += 1
        else:
            count_dict[sublist_tuple] = 1
    return count_dict

assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]) == {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
```

The `unique_sublists` function takes a list as input and counts the occurrences of each sublist within the list. It uses a dictionary to store the counts, where the key is a tuple representation of the sublist and the value is the number of occurrences. The function then returns the count dictionary.

The provided assertion checks if the function produces the expected output for the given example.