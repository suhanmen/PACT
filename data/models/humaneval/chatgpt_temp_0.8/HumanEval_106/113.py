python
def f(n):
    lst = []
    for i in range(1, n+1):
        if i % 2 == 0:
            fact = 1
            for j in range(1, i+1):
                fact *= j
            lst.append(fact)
        else:
            lst.append(sum(range(1, i+1)))
    return lst
