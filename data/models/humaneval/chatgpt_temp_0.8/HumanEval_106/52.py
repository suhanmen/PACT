def f(n):
    result = []
    factorial = 1
    total = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            factorial *= i
            result.append(factorial)
        else:
            total += i
            result.append(total)
    return result
