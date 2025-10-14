Here is the completed code snippet:

```python
def get_pairs_count(nums, target_sum):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target_sum:
                count += 1
    return count

assert get_pairs_count([1,1,1,1], 2) == 6
```

In this code, the `get_pairs_count` function takes a list of numbers (`nums`) and a target sum (`target_sum`) as input. It initializes a variable `count` to keep track of the number of pairs whose sum is equal to the target sum.

The function then uses nested loops to iterate through all possible pairs of numbers in the list. For each pair, it checks if the sum of the two numbers is equal to the target sum. If it is, it increments the `count` variable.

Finally, the function returns the `count` variable, which represents the number of pairs whose sum is equal to the target sum.

The code also includes an assertion to verify that the function returns the expected result for the given example input.