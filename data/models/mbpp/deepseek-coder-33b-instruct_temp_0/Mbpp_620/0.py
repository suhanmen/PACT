Here is the Python function implemented in a markdown style code block:

```python
def largest_subset(nums):
    """
    Write a function to find the size of the largest subset of a list of numbers so that every pair is divisible.
    """
    nums.sort()
    divisors = [-1] * len(nums)
    previous = [-1] * len(nums)
    max_index = 0

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                if divisors[i] < divisors[j] + 1:
                    divisors[i] = divisors[j] + 1
                    previous[i] = j
        if divisors[max_index] < divisors[i]:
            max_index = i

    result = []
    current = max_index
    while current >= 0:
        result.append(nums[current])
        current = previous[current]

    return len(result)

# Test the function
print(largest_subset([ 1, 3, 6, 13, 17, 18 ]))  # Output: 4
```

This function works by first sorting the input list. Then it initializes two lists, `divisors` and `previous`, with the same length as the input list. The `divisors` list stores the size of the largest subset ending at each index, and the `previous` list stores the index of the previous number in the largest subset.

The function then iterates over the sorted list, and for each number, it checks all previous numbers to see if the current number is divisible by them. If it is, and the size of the largest subset ending at the current number is less than the size of the largest subset ending at the previous number plus one, it updates the `divisors` and `previous` lists.

Finally, it finds the index of the largest subset, and constructs the subset by following the `previous` list from the largest index. The function then returns the size of the largest subset.
