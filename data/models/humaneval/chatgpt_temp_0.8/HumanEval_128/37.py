def prod_signs(arr):
    if not arr:
        return None
    product = 1
    sum_magnitudes = 0
    for num in arr:
        sign = 0 if num == 0 else abs(num) // num
        product *= sign
        sum_magnitudes += abs(num)
    return product * sum_magnitudes
