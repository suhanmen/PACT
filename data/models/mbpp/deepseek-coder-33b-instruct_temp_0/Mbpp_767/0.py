Here is the Python function to solve the problem:

```python
def get_pairs_count(numbers, sum):
    count = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == sum:
                count += 1
    return count
```

This function works by iterating over each pair of numbers in the list. If the sum of a pair equals the target sum, it increments a counter. The function finally returns the counter, which represents the number of pairs whose sum equals the target sum.

You can test the function with the following code:

```python
print(get_pairs_count([1,1,1,1],2))  # Output: 6
```

This will output `6`, which is the expected result.
