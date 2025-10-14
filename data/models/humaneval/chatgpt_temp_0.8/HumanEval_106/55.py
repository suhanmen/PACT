def f(n):
    res = []
    factorial = 1
    for i in range(1, n+1):
        if i % 2 == 0:
            res.append(factorial)
            factorial *= (i+1)
        else:
            res.append(sum(range(1, i+1)))
    return res
