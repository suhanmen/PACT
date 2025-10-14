Here's the completed code snippet:

```python
def cal_sum(n):
    perrin = [3, 0, 2]
    if n <= 2:
        return sum(perrin[:n+1])
    else:
        for i in range(3, n+1):
            perrin.append(perrin[i-2] + perrin[i-3])
        return sum(perrin)

assert cal_sum(9) == 49
```

In this code, we define a function `cal_sum` that takes an integer `n` as input. The function calculates the sum of the first `n` Perrin numbers.

The Perrin sequence is a sequence of numbers where each number is the sum of the previous two numbers, similar to the Fibonacci sequence. The first three numbers in the Perrin sequence are 3, 0, and 2.

If `n` is less than or equal to 2, we simply return the sum of the first `n+1` numbers in the Perrin sequence.

If `n` is greater than 2, we use a loop to calculate the remaining numbers in the Perrin sequence and append them to the `perrin` list. Finally, we return the sum of all the numbers in the `perrin` list.

The `assert` statement at the end of the code snippet verifies that `cal_sum(9)` returns the expected result of 49.