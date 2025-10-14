def f(n):
    result = []
    factorial = 1
    total = 0
    for i in range(n):
        if i % 2 == 0:
            if i == 0:
                result.append(factorial)
            else:
                factorial *= i
                result.append(factorial)
        else:
            total += i
            result.append(total)
    return result
