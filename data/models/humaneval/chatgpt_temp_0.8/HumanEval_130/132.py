def tri(n):
    res = []
    if n == 0:
        return [0]
    elif n == 1:
        return [3]
    elif n == 2:
        return [3, 1]
    else:
        res = [3, 1, 2]
        for i in range(3, n+1):
            if i % 2 == 0:
                res.append(1 + i // 2)
            else:
                res.append(res[i-1] + res[i-2] + res[i+1])
    return res
