def f(n):
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            # calculate the factorial of i if i is even
            fact = 1
            for j in range(1, i+1):
                fact *= j
            result.append(fact)
        else:
            # calculate the sum of numbers from 1 to i if i is odd
            s = 0
            for j in range(1, i+1):
                s += j
            result.append(s)
    return result
