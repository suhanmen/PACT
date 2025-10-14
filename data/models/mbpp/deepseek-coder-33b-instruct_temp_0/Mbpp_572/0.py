Here is the Python function to remove duplicate numbers from a given number of lists:

```python
def two_unique_nums(nums):
    num_counts = {}
    for num in nums:
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1
    unique_nums = [num for num, count in num_counts.items() if count == 1]
    return unique_nums

print(two_unique_nums([1,2,3,2,3,4,5]))  # Output: [1, 4, 5]
```

This function works by first creating a dictionary where the keys are the numbers in the list and the values are the counts of each number. It then creates a new list of numbers that only appear once in the original list.
