Here is the completed code snippet:

```python
def cube_Sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += (2*i)**3
    return sum

assert cube_Sum(2) == 72
```

In this code, the function `cube_Sum` takes an integer `n` as input and calculates the cube sum of the first `n` even natural numbers. It uses a for loop to iterate from 1 to `n` and adds the cube of each even number to the `sum` variable. Finally, it returns the total sum.

The `assert` statement is used to check if the function returns the expected result. In this case, it checks if `cube_Sum(2)` is equal to 72. If the condition is true, the code continues execution. If the condition is false, an AssertionError is raised.