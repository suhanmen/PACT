Here is the completed code snippet:

```python
def max_sum_list(lst):
    max_sum = float('-inf')
    max_list = []
    
    for sublist in lst:
        sublist_sum = sum(sublist)
        if sublist_sum > max_sum:
            max_sum = sublist_sum
            max_list = sublist
    
    return max_list

assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]) == [10, 11, 12]
```

In this code, we define a function `max_sum_list` that takes a list of lists as input. We initialize `max_sum` to negative infinity and `max_list` to an empty list.

We then iterate over each sublist in the input list. For each sublist, we calculate the sum of its elements using the `sum` function. If the sum is greater than the current maximum sum (`max_sum`), we update `max_sum` and `max_list` to the current sublist.

Finally, we return `max_list`, which will be the sublist with the highest sum of elements.

The `assert` statement at the end of the code verifies that the function returns the expected result for the given example input.