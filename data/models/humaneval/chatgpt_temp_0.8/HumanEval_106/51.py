def f(n):
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            # if i is even, calculate its factorial
            factorial = 1
            for j in range(1, i+1):
                factorial *= j
            result.append(factorial)
        else:
            # if i is odd, calculate the sum of numbers from 1 to i
            sum = 0
            for j in range(1, i+1):
                sum += j
            result.append(sum)
    return result
