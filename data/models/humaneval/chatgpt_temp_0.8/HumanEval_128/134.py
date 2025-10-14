def prod_signs(arr):
    if not arr:
        return None
    product_sign = 1
    magnitude_sum = 0
    for num in arr:
        if num == 0:
            product_sign = 0
        elif num < 0:
            product_sign *= -1
        magnitude_sum += abs(num)
    return magnitude_sum * product_sign
