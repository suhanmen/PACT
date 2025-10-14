Here's the completed code snippet:

```python
def jacobsthal_num(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for _ in range(2, n+1):
            c = 2*b + a
            a = b
            b = c
        return b

assert jacobsthal_num(5) == 11
```

This function calculates the nth Jacobsthal number using a loop. It starts with the base cases of n=0 and n=1, and then iteratively calculates the next number in the sequence using the formula `c = 2*b + a`, where `a` and `b` are the previous two numbers in the sequence. Finally, it returns the nth Jacobsthal number.