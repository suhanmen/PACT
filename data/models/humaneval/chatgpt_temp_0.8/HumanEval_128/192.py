def prod_signs(arr):
    if not arr:
        return None
    prod = 1
    sum_mag = 0
    for num in arr:
        if num > 0:
            prod *= 1
            sum_mag += num
        elif num < 0:
            prod *= -1
            sum_mag += abs(num)
        else:
            prod *= 0
    return prod * sum_mag
