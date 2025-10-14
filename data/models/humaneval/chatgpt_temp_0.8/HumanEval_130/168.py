def tri(n):
    res = []
    if n == 0:
        return res
    res.append(3)
    if n == 1:
        return res
    res.append(1 + n//2)
    if n == 2:
        return res
    for i in range(3, n + 1):
        if i % 2 == 0:
            res.append(1 + i//2)
        else:
            res.append(res[-1] + res[-2] + res[-3])
    return res
