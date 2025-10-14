def prod_signs(arr):
    if not arr:
        return None
    prod = 1
    sign_sum = 0
    for num in arr:
        if num > 0:
            sign = 1
        elif num < 0:
            sign = -1
        else:
            sign = 0
        prod *= sign
        sign_sum += abs(num)
    return prod * sign_sum
