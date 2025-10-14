Here is the completed code snippet:

```python
def get_median(list1, list2, size):
    merged_list = list1 + list2
    merged_list.sort()
    
    if size % 2 == 0:
        median = (merged_list[size//2 - 1] + merged_list[size//2]) / 2
    else:
        median = merged_list[size//2]
    
    return median

assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
```

The `get_median` function takes in two sorted lists (`list1` and `list2`) and the size of the lists (`size`). It merges the two lists into one sorted list using the `+` operator and the `sort` method. 

Then, it checks if the size of the merged list is even or odd. If it is even, it calculates the median by taking the average of the two middle elements. If it is odd, it simply takes the middle element as the median.

Finally, the function returns the median.

The `assert` statement at the end checks if the function returns the expected median for the given example.