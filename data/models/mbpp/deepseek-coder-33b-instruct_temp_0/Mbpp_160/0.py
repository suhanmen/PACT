Here is the Python function that solves the problem:

```python
def find_solution(a, b, n):
    for x in range(n+1):
        for y in range(n+1):
            if a*x + b*y == n:
                return (x, y)
    return None
```

This function uses a brute force approach to find the solution. It iterates over all possible values of x and y from 0 to n, and checks if the equation `ax + by = n` holds for each pair of x and y. If it does, the function returns the pair as a tuple. If no solution is found after checking all possible pairs, the function returns `None`.

Please note that this function has a time complexity of O(n^2), which may not be efficient for large values of n. There are more efficient algorithms for solving this problem, such as the extended Euclidean algorithm, but they are more complex and beyond the scope of this problem.
