def f(n):
    result = []  # initialize an empty list to store the result
    for i in range(1, n+1):
        if i % 2 == 0:  # if i is even
            factorial = 1
            for j in range(1, i+1):
                factorial *= j  # compute the factorial of i
            result.append(factorial)  # add the factorial to the result list
        else:  # if i is odd
            total = 0
            for j in range(1, i+1):
                total += j  # compute the sum of numbers from 1 to i
            result.append(total)  # add the total to the result list
    return result
