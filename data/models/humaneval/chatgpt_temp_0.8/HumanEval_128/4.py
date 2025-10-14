def prod_signs(arr):
    if not arr:
        return None
    sign = 1
    magnitude_sum = 0
    for num in arr:
        if num > 0:
            magnitude_sum += num
        elif num < 0:
            magnitude_sum += abs(num)
            sign *= -1
    return magnitude_sum * sign
