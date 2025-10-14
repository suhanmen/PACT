def f(n):
    res = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            fact = 1
            for j in range(1, i + 1):
                fact *= j
            res.append(fact)
        else:
            res.append(sum(range(1, i + 1)))
    return res
