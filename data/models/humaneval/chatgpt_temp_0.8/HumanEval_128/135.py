def prod_signs(arr):
    if not arr:
        return None
    sign_prod = 1
    mag_sum = 0
    for num in arr:
        if num > 0:
            sign_prod *= 1
            mag_sum += num
        elif num < 0:
            sign_prod *= -1
            mag_sum += abs(num)
        else:
            sign_prod *= 0
    return sign_prod * mag_sum
