def prod_signs(arr):
    if not arr:
        return None
    product = 1
    magnitude_sum = 0
    for num in arr:
        sign = 0 if num == 0 else (1 if num > 0 else -1)
        product *= sign
        magnitude_sum += abs(num)
    return product * magnitude_sum
