def f(n):
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            fact = 1
            for j in range(1, i+1):
                fact *= j
            result.append(fact)
        else:
            result.append(sum(range(1, i+1)))
    return result
