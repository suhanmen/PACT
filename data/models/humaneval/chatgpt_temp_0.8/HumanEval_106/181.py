def f(n):
    result = []
    for i in range(1,n+1):
        if i%2 == 0: # i is even
            fact = 1
            for j in range(1,i+1):
                fact *= j
            result.append(fact)
        else: # i is odd
            s = 0
            for j in range(1,i+1):
                s += j
            result.append(s)
    return result
