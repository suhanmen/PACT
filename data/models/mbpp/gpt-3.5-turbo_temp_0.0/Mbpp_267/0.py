Here is the completed code snippet:

```python
def square_Sum(n):
    sum = 0
    for i in range(1, 2*n, 2):
        sum += i**2
    return sum

assert square_Sum(2) == 10
```

In this code, we define a function `square_Sum` that takes in an integer `n`. We initialize a variable `sum` to 0 to keep track of the sum of the squares. 

We then use a for loop to iterate over the range from 1 to 2*n (exclusive) with a step of 2. This ensures that we only consider the odd natural numbers. 

Inside the loop, we add the square of each odd number to the `sum` variable. Finally, we return the `sum` as the result.

The `assert` statement is used to verify that the function returns the expected result for the given input.