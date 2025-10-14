Here is the Python function to find the second smallest number in a list:

```python
def second_smallest(nums):
    m1, m2 = float('inf'), float('inf')
    for x in nums:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m2
```

This function works by initializing two variables, `m1` and `m2`, to infinity. It then iterates over the list of numbers. If a number is less than or equal to `m1`, it updates `m1` and `m2` to that number and the previous `m1`. If a number is greater than `m1` but less than `m2`, it updates `m2` to that number. At the end of the function, `m2` will be the second smallest number in the list.
