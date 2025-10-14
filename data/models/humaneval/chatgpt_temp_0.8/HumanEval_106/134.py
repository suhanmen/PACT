def f(n):
    res = []
    fact = 1
    s = 0
    for i in range(n):
        if i % 2 == 0:
            res.append(fact)
            fact *= (i + 1)
        else:
            s += (i + 1)
            res.append(s)
    return res
