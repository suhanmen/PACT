def prod_signs(arr):
    if len(arr) == 0:
        return None
    prod = 1
    total_mag = 0
    for num in arr:
        if num > 0:
            prod *= 1
            total_mag += num
        elif num < 0:
            prod *= -1
            total_mag += abs(num)
        else:
            prod *= 0
    return prod * total_mag
