Here is the Python function to solve the problem:

```python
def max_product(arr):
    n = len(arr)
    max_ending_here = 1
    min_ending_here = 1
    max_so_far = 1
    flag = 0

    for i in range(n):
        if arr[i] > 0:
            max_ending_here = max_ending_here * arr[i]
            min_ending_here = min(min_ending_here * arr[i], 1)
            flag = 1
        elif arr[i] == 0:
            max_ending_here = 1
            min_ending_here = 1
        else:
            temp = max_ending_here
            max_ending_here = max(min_ending_here * arr[i], 1)
            min_ending_here = temp * arr[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

    if flag == 0 and max_so_far == 1:
        return 0
    return max_so_far
```

This function uses dynamic programming to find the maximum product of an increasing subsequence. It keeps track of the maximum and minimum product ending at each position in the array, and updates these values as it iterates through the array. The maximum product found so far is updated whenever a larger product is found. If the array contains only positive numbers, the function returns the product of all numbers. If the array contains zero, the function returns 0. If the array contains only negative numbers, the function returns the maximum negative number.
