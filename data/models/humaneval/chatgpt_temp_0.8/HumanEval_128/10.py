def prod_signs(arr):
    if len(arr) == 0:
        return None
    prod = 1
    mag_sum = 0
    for num in arr:
        if num > 0:
            prod *= 1
            mag_sum += num
        elif num < 0:
            prod *= -1
            mag_sum += abs(num)
        else:
            prod *= 0
    return prod * mag_sum
