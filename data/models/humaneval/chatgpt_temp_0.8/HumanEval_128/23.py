def prod_signs(arr):
    if not arr:
        return None
    sign_prod = 1
    mag_sum = 0
    for num in arr:
        if num == 0:
            sign_prod = 0
        else:
            sign_prod *= 1 if num > 0 else -1
            mag_sum += abs(num)
    return sign_prod * mag_sum
