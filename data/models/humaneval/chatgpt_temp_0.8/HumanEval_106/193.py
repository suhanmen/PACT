def f(n):
    res = []
    for i in range(1, n+1):
        if i % 2 == 0:
            # calculate the factorial of i
            fact = 1
            for j in range(1, i+1):
                fact *= j
            res.append(fact)
        else:
            # calculate the sum of numbers from 1 to i
            s = 0
            for j in range(1, i+1):
                s += j
            res.append(s)
    return res
