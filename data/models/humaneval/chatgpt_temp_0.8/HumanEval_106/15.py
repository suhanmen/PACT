def f(n):
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            # calculate the factorial of i
            fact = 1
            for j in range(1, i+1):
                fact *= j
            result.append(fact)
        else:
            # calculate the sum of numbers from 1 to i
            total = 0
            for j in range(1, i+1):
                total += j
            result.append(total)
    return result
