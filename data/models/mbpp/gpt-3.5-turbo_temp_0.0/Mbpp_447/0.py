Here is the completed code snippet:

```python
def cube_nums(nums):
    return [num**3 for num in nums]

assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```

The `cube_nums` function takes a list of numbers as input and returns a new list containing the cubes of each individual element in the input list. The list comprehension `[num**3 for num in nums]` is used to iterate over each element in the input list and calculate its cube using the exponentiation operator `**`. The resulting list of cubes is then returned. The `assert` statement is used to verify that the function produces the expected output for the given example.