Here is the completed code snippet:

```python
def remove_kth_element(lst, k):
    return lst[:k-1] + lst[k:]

assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]
```

In this code, the `remove_kth_element` function takes two parameters: `lst`, which is the input list, and `k`, which is the index of the element to be removed. 

The function returns a new list that is created by concatenating two slices of the original list: `lst[:k-1]` and `lst[k:]`. The first slice includes all elements from the beginning of the list up to the element before the k'th element, and the second slice includes all elements after the k'th element. This effectively removes the k'th element from the list.

The `assert` statement is used to verify that the function produces the expected output for the given example.