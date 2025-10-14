def f(n):
    result = []
    factorial = 1
    for i in range(1, n + 1):
        if i % 2 == 0:
            result.append(factorial)
            factorial *= i + 1
        else:
            result.append(sum(range(1, i + 1)))
    return result
