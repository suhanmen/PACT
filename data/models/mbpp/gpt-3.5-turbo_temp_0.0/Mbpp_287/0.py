Here is the completed code snippet:

```python
def square_Sum(n):
    sum_of_squares = 0
    for i in range(1, n+1):
        sum_of_squares += (2*i)**2
    return sum_of_squares

assert square_Sum(2) == 20
```

In this code, the function `square_Sum` takes in an integer `n` as a parameter. It initializes a variable `sum_of_squares` to 0. Then, it iterates over the range from 1 to `n+1` (inclusive) using a for loop. For each iteration, it calculates the square of the current even number (2*i) and adds it to the `sum_of_squares` variable. Finally, it returns the `sum_of_squares` value.

The `assert` statement is used to check if the function returns the expected result for the given input. In this case, it checks if `square_Sum(2)` returns 20. If the assertion is true, the code will continue executing without any output. If the assertion is false, it will raise an AssertionError.