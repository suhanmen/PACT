def f(n):
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            # Compute the factorial of i
            factorial = 1
            for j in range(1, i+1):
                factorial *= j
            result.append(factorial)
        else:
            # Compute the sum of numbers from 1 to i
            result.append(sum(range(1, i+1)))
    return result
