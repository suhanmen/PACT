Here is the Python function to move all zeroes to the end of the given list:

```python
def move_zero(nums):
    for i in nums:
        if i == 0:
            nums.remove(i)
            nums.append(i)
    return nums
```

You can test the function with the following code:

```python
print(move_zero([1,0,2,0,3,4]))  # Output: [1, 2, 3, 4, 0, 0]
```

This function works by iterating over the list and checking each element. If the element is zero, it removes it from the list and appends it at the end. This way, all zeroes are moved to the end of the list.
