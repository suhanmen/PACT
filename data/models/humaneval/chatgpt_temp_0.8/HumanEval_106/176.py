def f(n):
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            # calculate factorial
            factorial = 1
            for j in range(1, i+1):
                factorial *= j
            result.append(factorial)
        else:
            # calculate sum of numbers from 1 to i
            total = 0
            for j in range(1, i+1):
                total += j
            result.append(total)
    return result
