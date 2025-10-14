def prod_signs(arr):
    if len(arr) == 0:
        return None
    
    signs_product = 1
    magnitude_sum = 0
    for num in arr:
        if num > 0:
            signs_product *= 1
            magnitude_sum += num
        elif num < 0:
            signs_product *= -1
            magnitude_sum += abs(num)
        else:
            signs_product *= 0
    
    return signs_product * magnitude_sum
