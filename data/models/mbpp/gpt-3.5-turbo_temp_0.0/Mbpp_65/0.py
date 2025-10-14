Here is the completed code snippet:

```python
def recursive_list_sum(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += recursive_list_sum(item)
        else:
            total += item
    return total

assert recursive_list_sum(([1, 2, [3,4],[5,6]])) == 21
```

The `recursive_list_sum` function takes a list as input and recursively sums all of its elements. If an element is itself a list, the function calls itself on that sublist to get the sum of its elements. If an element is not a list, it is simply added to the total. The function returns the final sum. The provided test case asserts that the function correctly sums the elements of the given list to equal 21.