def prod_signs(arr):
    if not arr:
        return None
    
    prod_sign = 1
    magnitude_sum = 0
    
    for num in arr:
        if num == 0:
            prod_sign = 0
        elif num > 0:
            prod_sign *= 1
            magnitude_sum += num
        else:
            prod_sign *= -1
            magnitude_sum += abs(num)
    
    return prod_sign * magnitude_sum
