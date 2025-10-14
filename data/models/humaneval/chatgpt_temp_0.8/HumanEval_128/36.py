def prod_signs(arr):
    if not arr:
        return None
    prod = 1
    sum_mag = 0
    for num in arr:
        if num == 0:
            continue
        prod *= num / abs(num)
        sum_mag += abs(num)
    return int(prod * sum_mag)
