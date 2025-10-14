def prod_signs(arr):
    if len(arr) == 0:
        return None
    prod_sign = 1
    sum_magnitudes = 0
    for num in arr:
        if num == 0:
            prod_sign = 0
            continue
        prod_sign *= num / abs(num)
        sum_magnitudes += abs(num)
    return prod_sign * sum_magnitudes
