Here is the Python function to count the pairs of reverse strings in the given string list:

```python
def count_reverse_pairs(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i][::-1] == lst[j]:
                count += 1
    return count

print(count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"]))
```

This function works by iterating over each string in the list and comparing it with every other string in the list. If the reverse of the current string is equal to another string in the list, it increments the count. The function finally returns the count of reverse pairs.
