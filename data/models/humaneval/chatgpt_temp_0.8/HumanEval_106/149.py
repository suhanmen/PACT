def f(n):
    result = []
    factorial = 1
    for i in range(n):
        if i % 2 == 0: # if i is even
            result.append(factorial)
            factorial *= (i+1)
        else: # if i is odd
            result.append(sum(range(1, i+2)))
    return result
