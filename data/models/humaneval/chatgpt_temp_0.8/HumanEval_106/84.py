def f(n):
    """
    Returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    """
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            # Compute the factorial of i
            fact = 1
            for j in range(1, i+1):
                fact *= j
            result.append(fact)
        else:
            # Compute the sum of numbers from 1 to i
            total = 0
            for j in range(1, i+1):
                total += j
            result.append(total)
    return result
