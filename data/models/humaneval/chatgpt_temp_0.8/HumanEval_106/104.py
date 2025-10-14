def f(n):
    result = []
    fact = 1
    sum_numbers = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            fact *= i
            result.append(fact)
        else:
            sum_numbers += i
            result.append(sum(range(1, i+1)))
    return result
