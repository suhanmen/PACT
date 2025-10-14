Here is the Python function to find the sum of fourth power of first n odd natural numbers:

```python
def odd_num_sum(n):
    sum = 0
    num = 1
    for i in range(n):
        sum += num ** 4
        num += 2
    return sum
```

You can test the function with the following code:

```python
print(odd_num_sum(2))  # Output: 82
```

This function works by initializing a variable `sum` to 0 and `num` to 1. It then enters a loop that runs `n` times. In each iteration of the loop, it adds the fourth power of `num` to `sum` and then increments `num` by 2 to get the next odd number. Finally, it returns the sum.
