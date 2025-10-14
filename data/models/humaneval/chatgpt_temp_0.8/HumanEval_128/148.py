def prod_signs(arr):
    if not arr:
        return None
    prod = 1
    mag_sum = 0
    for num in arr:
        if num == 0:
            prod = 0
        else:
            prod *= num / abs(num)
        mag_sum += abs(num)
    return int(prod * mag_sum)
