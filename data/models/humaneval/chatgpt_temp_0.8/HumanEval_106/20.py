def f(n):
    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            value = 1
            for j in range(1, i + 1):
                value *= j
            result.append(value)
        else:
            value = sum(range(1, i + 1))
            result.append(value)
    return result
