def prod_signs(arr):
    if not arr:
        return None
    product_signs = 1
    sum_magnitudes = 0
    for num in arr:
        if num == 0:
            product_signs = 0
        else:
            product_signs *= 1 if num > 0 else -1
            sum_magnitudes += abs(num)
    return product_signs * sum_magnitudes
