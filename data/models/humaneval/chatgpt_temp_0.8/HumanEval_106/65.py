def f(n):
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            # calculate factorial of i
            fact = 1
            for j in range(1, i+1):
                fact *= j
            result.append(fact)
        else:
            # calculate sum of numbers from 1 to i
            s = sum(range(1, i+1))
            result.append(s)
    return result
