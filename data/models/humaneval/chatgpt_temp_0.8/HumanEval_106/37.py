def f(n):
    result = []
    for i in range(1, n+1):
        if i % 2 == 0: # if i is even
            fact = 1
            for j in range(1, i+1):
                fact *= j # calculate the factorial
            result.append(fact)
        else: # if i is odd
            result.append(sum(range(1, i+1))) # calculate the sum of numbers from 1 to i
    return result
