def prod_signs(arr):
    if not arr:
        return None
    sign_prod = 1
    mag_sum = 0
    for num in arr:
        mag_sum += abs(num)
        if num < 0:
            sign_prod *= -1
        elif num == 0:
            sign_prod = 0
    return mag_sum * sign_prod
