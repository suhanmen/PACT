Here is the completed code snippet:

```python
def find_Average_Of_Cube(n):
    sum_of_cubes = 0
    for i in range(1, n+1):
        sum_of_cubes += i**3
    average = sum_of_cubes / n
    return average

assert find_Average_Of_Cube(2) == 4.5
```

In this code, we define a function `find_Average_Of_Cube` that takes an integer `n` as input. We initialize a variable `sum_of_cubes` to keep track of the sum of cubes of the first `n` natural numbers. We then use a for loop to iterate from 1 to `n` and add the cube of each number to `sum_of_cubes`. After the loop, we calculate the average by dividing `sum_of_cubes` by `n` and return the result. Finally, we use an assert statement to check if the function returns the expected result for the given test case.