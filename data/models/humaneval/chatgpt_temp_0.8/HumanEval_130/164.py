def tri(n):
    res = [3]
    if n == 0:
        return res
    a, b, c, d = 1, 1, 3, 2
    while len(res) <= n:
        if len(res) % 2 == 1:
            res.append(d)
            d = a + b + c
            a, b, c = b, c, d
        else:
            res.append(1 + len(res) // 2)
    return res
