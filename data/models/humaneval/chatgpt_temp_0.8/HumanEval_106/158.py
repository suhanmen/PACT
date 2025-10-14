def f(n):
    result = []
    for i in range(n):
        if i % 2 == 0:
            # calculate factorial of i
            fact = 1
            for j in range(1, i+1):
                fact *= j
            result.append(fact)
        else:
            # calculate sum of numbers from 1 to i
            summation = sum(list(range(1, i+1)))
            result.append(summation)
    return result
