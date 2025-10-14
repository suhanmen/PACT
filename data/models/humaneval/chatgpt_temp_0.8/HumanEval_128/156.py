def prod_signs(arr):
    if not arr:
        return None
    sign = 1
    magnitudes_sum = 0
    for num in arr:
        if num == 0:
            sign = 0
        else:
            sign *= num / abs(num)
            magnitudes_sum += abs(num)
    return sign * magnitudes_sum
