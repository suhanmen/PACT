def prod_signs(arr):
    if len(arr) == 0:
        return None
    magnitude_sum = 0
    sign_product = 1
    for num in arr:
        sign = 1 if num > 0 else -1 if num < 0 else 0
        magnitude_sum += abs(num)
        sign_product *= sign
    return magnitude_sum * sign_product
