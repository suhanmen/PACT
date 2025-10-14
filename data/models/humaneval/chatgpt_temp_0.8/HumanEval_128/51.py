def prod_signs(arr):
    if not arr:
        return None
    sign_prod = 1
    magnitude_sum = 0
    for num in arr:
        if num > 0:
            sign_prod *= 1
        elif num < 0:
            sign_prod *= -1
        else:
            sign_prod *= 0
        magnitude_sum += abs(num)
    return sign_prod * magnitude_sum
