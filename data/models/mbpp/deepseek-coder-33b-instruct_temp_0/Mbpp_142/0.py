Here is the Python function that solves the problem:

```python
def count_samepair(list1, list2, list3):
    count = 0
    for i in range(len(list1)):
        if list1[i] == list2[i] == list3[i]:
            count += 1
    return count
```

You can test the function with the provided example:

```python
print(count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9]))  # Output: 3
```

This function works by iterating over the indices of the first list. For each index, it checks if the elements at the same index in the other two lists are identical. If they are, it increments a counter. Finally, it returns the counter, which represents the number of identical elements in the same position in all three lists.
