def prod_signs(arr):
    if not arr:
        return None
    sign_product = 1
    mag_sum = 0
    for num in arr:
        if num > 0:
            mag_sum += num
        elif num < 0:
            mag_sum += abs(num)
            sign_product *= -1
        else:
            pass
    return sign_product * mag_sum
