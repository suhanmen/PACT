def prod_signs(arr):
    if len(arr) == 0:
        return None
    sign = 1
    total = 0
    for num in arr:
        if num == 0:
            return 0
        total += abs(num)
        sign *= -1 if num < 0 else 1
    return total * sign
