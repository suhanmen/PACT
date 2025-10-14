def prod_signs(arr):
    if not arr:
        return None
    product = 1
    sum_magnitudes = 0
    for num in arr:
        sign = 1 if num > 0 else -1 if num < 0 else 0
        product *= sign
        sum_magnitudes += abs(num)
    return product * sum_magnitudes
