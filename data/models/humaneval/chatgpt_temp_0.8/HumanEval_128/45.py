def prod_signs(arr):
    if not arr:
        return None
    prod = 1
    sum_abs = 0
    for num in arr:
        if num == 0:
            prod = 0
        elif num > 0:
            prod *= 1
            sum_abs += num
        else:
            prod *= -1
            sum_abs += abs(num)
    return prod * sum_abs
