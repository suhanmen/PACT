Here is the Python function to pack consecutive duplicates of a given list elements into sublists:

```python
def pack_consecutive_duplicates(lst):
    packed = []
    for num in lst:
        if packed and num == packed[-1][0]:
            packed[-1].append(num)
        else:
            packed.append([num])
    return packed
```

This function works by iterating over the input list. For each number, it checks if the last sublist in the packed list is for the same number. If it is, it appends the number to that sublist. If it's not, it starts a new sublist for that number.

You can test this function with the provided test case:

```python
print(pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]))
```

This should output:

```python
[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
```
