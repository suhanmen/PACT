Here is the Python function to find the nth number in the Newman Conway Sequence:

```python
def sequence(n):
    if n == 1 or n == 2:
        return 1
    else:
        p = [0, 1, 1]
        for i in range(3, n+1):
            p.append(p[p[i-1]] + p[i - p[i-1]])
        return p[n]

# Test the function
print(sequence(10))  # Output: 6
```

This function uses dynamic programming to build up the sequence. It starts with the base cases of `p[1]` and `p[2]` being 1, and then for each subsequent number `i`, it calculates `p[i]` as the sum of `p[p[i-1]]` and `p[i - p[i-1]]`. The result is stored in the list `p`, and the function returns the nth number in the sequence.
