Here is the completed code snippet:

```python
def split_two_parts(lst, L):
    return lst[:L], lst[L:]

assert split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])
```

The function `split_two_parts` takes in a list `lst` and an integer `L`. It uses list slicing to split the list into two parts: the first part contains the elements from index 0 to index `L-1`, and the second part contains the elements from index `L` to the end of the list. The function then returns these two parts as a tuple.