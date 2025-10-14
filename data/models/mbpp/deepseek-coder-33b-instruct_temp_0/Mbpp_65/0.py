Here is the Python function to flatten a list and sum all of its elements:

```python
def recursive_list_sum(lst):
    total = 0
    for i in lst:
        if type(i) == list:
            total += recursive_list_sum(i)
        else:
            total += i
    return total

# Test the function
print(recursive_list_sum([1, 2, [3,4],[5,6]]))  # Output: 21
```

This function works by iterating over each element in the list. If the element is a list, it calls itself recursively to flatten the sublist and add its sum to the total. If the element is not a list, it adds the element to the total.
