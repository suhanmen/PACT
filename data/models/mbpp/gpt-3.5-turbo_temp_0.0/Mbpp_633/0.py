Here is the completed code snippet:

```python
def pair_xor_Sum(nums, n):
    xor_sum = 0
    for i in range(n):
        for j in range(i+1, n):
            xor_sum += nums[i] ^ nums[j]
    return xor_sum

assert pair_xor_Sum([5,9,7,6],4) == 47
```

In this code, the function `pair_xor_Sum` takes two parameters: `nums`, which is the list of numbers, and `n`, which is the length of the list. 

The function uses two nested loops to iterate through all possible pairs of numbers in the list. For each pair, it calculates the XOR (exclusive OR) of the two numbers and adds it to the `xor_sum` variable. 

Finally, the function returns the `xor_sum` as the result. The `assert` statement is used to verify that the function returns the expected result for the given example.