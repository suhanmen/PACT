Here is the Python function to check whether a specified list is sorted or not:

```python
def issort_list(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

# Test the function
print(issort_list([1,2,4,6,8,10,12,14,16,17]))  # Output: True
```

In this function, we are using the `all()` function to check if all elements in the list satisfy the condition that the current element is less than or equal to the next element. If all elements satisfy this condition, the function returns `True`, indicating that the list is sorted. If any element does not satisfy this condition, the function returns `False`, indicating that the list is not sorted.
