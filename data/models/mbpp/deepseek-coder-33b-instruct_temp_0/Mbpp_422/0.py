Here is the Python function to find the average of cubes of first n natural numbers:

```python
def find_Average_Of_Cube(n):
    sum_of_cubes = sum(i**3 for i in range(1, n+1))
    average = sum_of_cubes / n
    return average
```

You can test the function with the following code:

```python
print(find_Average_Of_Cube(2))  # Output: 4.5
```

This function works by first calculating the sum of the cubes of the first n natural numbers using a generator expression. It then divides this sum by n to find the average.
