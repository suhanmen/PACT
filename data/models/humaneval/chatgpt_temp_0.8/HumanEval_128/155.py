def prod_signs(arr):
    if not arr:
        return None
    product = 1
    magnitude_sum = 0
    for num in arr:
        if num > 0:
            product *= 1
            magnitude_sum += num
        elif num < 0:
            product *= -1
            magnitude_sum += abs(num)
        else:
            product *= 0
    return product * magnitude_sum
