def prod_signs(arr):
    if not arr:
        return None
    sign = 1
    res = 0
    for num in arr:
        if num == 0:
            return 0
        res += abs(num)
        if num < 0:
            sign *= -1
    return res * sign
