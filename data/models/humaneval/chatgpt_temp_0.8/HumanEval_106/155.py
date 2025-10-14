def f(n):
    result = []
    factorial = 1
    for i in range(n):
        if i % 2 == 0:
            if i == 0:
                result.append(1)
            else:
                factorial = factorial * i
                result.append(factorial)
        else:
            result.append(sum(range(1, i+1)))
    return result
