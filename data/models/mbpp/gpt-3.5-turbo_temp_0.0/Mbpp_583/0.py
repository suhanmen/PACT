Here is the completed code snippet:

```python
def catalan_number(n):
    if n <= 1:
        return 1
    
    catalan = [0] * (n+1)
    catalan[0] = 1
    catalan[1] = 1
    
    for i in range(2, n+1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i-j-1]
    
    return catalan[n]

assert catalan_number(10) == 16796
```

The function `catalan_number` calculates the nth Catalan number using dynamic programming. It initializes a list `catalan` with all elements set to 0. Then, it sets the first two elements of `catalan` to 1. 

Next, it uses a nested loop to calculate the remaining Catalan numbers up to the nth number. The outer loop iterates from 2 to n, and the inner loop iterates from 0 to i-1. For each iteration, it calculates the Catalan number by multiplying the corresponding elements from the previous Catalan numbers.

Finally, the function returns the nth Catalan number.

The `assert` statement checks if `catalan_number(10)` returns the expected value of 16796.