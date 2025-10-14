def f(n):
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            factorial = 1
            for j in range(1, i+1):
                factorial *= j
            result.append(factorial)
        else:
            sum = 0
            for k in range(1, i+1):
                sum += k
            result.append(sum)
    return result
