Here is the completed code snippet:

```python
def pack_consecutive_duplicates(lst):
    packed_lst = []
    current_group = []
    
    for i in range(len(lst)):
        if i == 0 or lst[i] != lst[i-1]:
            if current_group:
                packed_lst.append(current_group)
            current_group = [lst[i]]
        else:
            current_group.append(lst[i])
    
    if current_group:
        packed_lst.append(current_group)
    
    return packed_lst

assert pack_consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]) == [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
```

The `pack_consecutive_duplicates` function takes a list `lst` as input and returns a new list where consecutive duplicates are packed into sublists. The function iterates through the input list and checks if the current element is the same as the previous element. If it is, the element is added to the current group. If it is not, the current group is added to the packed list and a new current group is started with the current element. Finally, if there is a remaining current group at the end of the iteration, it is also added to the packed list. The function then returns the packed list.

The assert statement at the end of the code snippet verifies that the function produces the expected output for the given example input.