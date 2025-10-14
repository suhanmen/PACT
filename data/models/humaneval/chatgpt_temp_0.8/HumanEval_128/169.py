def prod_signs(arr):
    if len(arr) == 0:
        return None
    product_of_signs = 1
    sum_of_magnitudes = 0
    for num in arr:
        if num == 0:
            product_of_signs = 0
        elif num > 0:
            product_of_signs *= 1
            sum_of_magnitudes += num
        else:
            product_of_signs *= -1
            sum_of_magnitudes += abs(num)
    return product_of_signs * sum_of_magnitudes
